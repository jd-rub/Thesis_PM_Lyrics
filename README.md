# Thesis_PM_Lyrics
This repository contains all code for the bachelor's thesis "Creating Song Lyrics using Natural Language Generation - A Comparison of Machine Learning Methods" by Justin Dettmer, written at Ruhr Universität Bochum.

## Dependencies
All dependencies can be found in `./requirements.txt`.  
Use `pip install -r ./requirements.txt` to install all required modules.  

## Usage
All results and corresponding corpora can be found in `./runs/`.  
Files without file extension are meant to be loaded with `pickle`.  

To reproduce results, use the `generate_*.py` scripts in the root folder.  
To re-train a model, use the `test_model_configs.py` script.  

Use the scripts in `/analysis/` to calculate the averages across the result csv files.

## Downloading Models
All trained models can be found at [Google Drive](https://drive.google.com/drive/folders/1g4v_n2TWhLhqS5x7kulG4xAuofwwkNEw?usp=sharing.) and will remain available until at least December 31st 2020. Longer availability will be provided if requested.
