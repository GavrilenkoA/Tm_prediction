# ProTDet


### Description

ProTDet is a machine learning tool designed to predict the melting temperature of proteins based on their sequence. It simplifies the process of accessing the thermostability of native proteins and provides an efficient solution for protein designers. With its advanced algorithms and accurate predictions, ProTDet empowers researchers and designers to make informed decisions in protein engineering and optimization.

### Usage

To start using ProTDet, follow the steps below:

1. Clone the ProTDet repository by running the following command:
    
    ```bash
    git clone git@github.com:GavrilenkoA/Tm_prediction.git
    ```
    
2. Install the required dependencies by creating a new conda environment and activating it:
    
    ```bash
    conda create -n protdet_env python=3.10.11
    conda activate protdet_env
    pip install -r requirements.txt
    ```
    
    This will create a new conda environment named protdet_env and install all the necessary dependencies specified in the requirements.txt
    file.
    
3. To launch the ProTDet tool and predict the melting temperature of a protein, use the following command:
    
    ```bash
    python3 inference/predict_tm.py <fasta_file>
    ```
    

	Note: Ensure that the FASTA file follows the standard format for protein sequences.

	Replace <fasta_file> with the path to your FASTA file containing the protein sequence you want to analyze. The tool will 	process the sequence and generate a tm_prediction.txt file containing the predicted melting temperature.

	Once the command completes execution, you will find the tm_prediction.txt file generated in the ROOT of directory. This file contains the predicted melting temperature for the provided protein sequence, along with the corresponding protein ID.

## Eda
1. [wget_filter.ipynb](./process_data/wget_filter.ipynb): Obtaining preprocessed mass spectrometry-based data encompassing melting temperatures of 34,925 proteins from 13 model organisms. To ensure data quality, duplicates were eliminated. Additionally, proteins longer than 1,020 amino acids were excluded as the transformer model has limitations on input sequence length.

[clustering.ipynb](./process_data/clustering.ipynb): The data has been categorized into three ordinal groups based on denaturation temperature. I have also calculated the statistical count for each category.
![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/3b596bbb-d509-49b2-bbcb-459bedea7206)

[eda_clusters.ipynb](./process_data/eda_clusters.ipynb) 
[feature_distribution.ipynb](./process_data/feature_distribution.ipynb) 



