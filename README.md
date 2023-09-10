
# Aksara Jawa-OCR
Welcome to the Aksara Jawa OCR project! This project focuses on implementing Optical Character Recognition (OCR) for Javanese aksara.

## Install
To install the Aksara Jawa OCR project, you can use the following command:

```bash
pip install .
```
This command will install the necessary dependencies and make the project accessible.

## Try It Out
You can try out the OCR simulation using Streamlit with the following commands:

```bash
cd service
streamlit run st_simulation.py
```
This will launch a Streamlit application for simulating the OCR process, allowing you to interact with the project and see it in action.

## Training

Our training process is based on the Adapting OCR repository, which you can find [here](https://github.com/Deepayan137/Adapting-OCR/tree/master). We've modified some of the training scripts to suit our needs.

`python -m train --name exp1 --path path/to/data --imgdir train`

* Main arguments
	* `--name`: creates a directory where checkpoints will be stored
	* `--path`: path to dataset. 
	* `--imgdir`: dir name of dataset

## Data 
Our dataset is available in our Kaggle repository, which you can access [here](https://www.kaggle.com/datasets/hermansugiharto/ocr-aksara-jawa). Feel free to use it for your OCR tasks.

## Contributions
We welcome contributions from the community to improve and expand this project. If you have any ideas, bug fixes, or enhancements, please feel free to contribute.

## About the Research Project

This project is part of our ongoing research efforts to make OCR for Aksara Jawa accessible to everyone. Our goal is to provide a powerful tool that can assist individuals in recognizing and processing Javanese aksara characters.

## Contact Information

If you have any questions, suggestions, or would like to contribute to our research project, please don't hesitate to reach out at [my email](mailto:hermansh.id@gmail.com). Your input and support are highly valued and will help us advance the field of Javanese aksara OCR.

Thank you for your interest in the Aksara Jawa OCR project! We look forward to collaborating with you.

## References

*  Training script are modified from [here](https://github.com/Deepayan137/Adapting-OCR/tree/master)