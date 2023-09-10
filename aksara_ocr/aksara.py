import torch
import os
import torch

from aksara_ocr.models.crnn import CRNN
from aksara_ocr.data.synth_dataset import SynthCollator
from aksara_ocr.utils.utils import Eval, OCRLabelConverter
from PIL import Image

import torchvision.transforms as transforms

class AksaraOCR:
    
    alphabet: str = """Only thewigsofrcvdampbkuq.$A-210xT5'MDL,RYHJ"ISPWENj&BC93VGFKz();#:!7U64Q8?+*ZX/%"""
    imgH: int = 32
    nChannels:int = 1
    nHidden:int = 256
    
    def __init__(self, verbose=False, device='cpu'):
        self.collate_fn = SynthCollator()
        self.converter = OCRLabelConverter(self.alphabet)
        self.evaluator = Eval()
        self.verbose = verbose
        self.device = device
        self.model = self.load_model()
        transform_list =  [transforms.Grayscale(1),
                    transforms.ToTensor(), 
                    transforms.Normalize((0.5,), (0.5,))]
        self.transform = transforms.Compose(transform_list)


    def load_model(self):
        try:
            model_arg = {    
                'imgH':self.imgH,
                'nChannels':self.nChannels,
                'nHidden':self.nHidden,
                'nClasses':len(self.alphabet)
            }        
            absolute_path = os.path.abspath(__file__)
            resume_file = os.path.join(os.path.dirname(absolute_path), "models", "best.ckpt")

            if self.verbose:
                print("\033[94mLoading model ...\033[0m")
            
            model = CRNN(model_arg)
            model = model.to(self.device)
            
            checkpoint = torch.load(resume_file, map_location=torch.device(self.device))
            model.load_state_dict(checkpoint['state_dict'])
            
            if self.verbose:
                print("\033[94mModel has been loaded %s.\033[0m" % self.device)
                
            return model
        
        except:
            print("\033[91mModel can't be loaded.\033[0m")
        

    def preprocessing_image(self, image):
        if self.verbose:
            print('Preprocess Image')
            
        img = self.transform(Image.open(image))
        single_image_data = [{'img': img, 'idx': 0}]    
        loader = torch.utils.data.DataLoader(single_image_data, batch_size=1, collate_fn=self.collate_fn)
        batch = next(iter(loader))
        input_ = batch['img'].to(self.device)
        return input_
    
    def predict(self, image):
        
        input_ = self.preprocessing_image(image)
        images = input_.squeeze().detach()
        
        if self.verbose:
            print("\033[94mPredicting image...\033[0m")
            
        logits = self.model(input_).transpose(1, 0)
        logits = torch.nn.functional.log_softmax(logits, 2)
        logits = logits.contiguous().cpu()
        T, B, _ = logits.size()
        pred_sizes = torch.LongTensor([T for _ in range(B)])
        _, pos = logits.max(2)
        pos = pos.transpose(1, 0).contiguous().view(-1)
        sim_preds = self.converter.decode(pos.data, pred_sizes.data, raw=False)
        if self.verbose:
            print("\033[94mImage predicted as %s.\033[0m" % sim_preds)
        
        return sim_preds, images