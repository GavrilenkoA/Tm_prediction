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

## EDA
1. [wget_filter.ipynb](./process_data/wget_filter.ipynb): Obtaining preprocessed mass spectrometry-based data encompassing melting temperatures of 34,925 proteins from 13 model organisms. To ensure data quality, duplicates were eliminated. Additionally, proteins longer than 1,020 amino acids were excluded as the transformer model has limitations on input sequence length.

2. [clustering.ipynb](./process_data/clustering.ipynb): The data has been categorized into three ordinal groups based on denaturation temperature. I have also calculated the statistical count for each category.
   
![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/3b596bbb-d509-49b2-bbcb-459bedea7206)

3. [feature_distribution.ipynb](./process_data/feature_distribution.ipynb)
We have computed the distributions of primary and tertiary structure features for proteins based on their ordinal category of denaturation temperature.
![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/4a46d603-fdee-488a-b87f-28dc10a92b06)
Proteins exhibiting higher denaturation temperatures are typically associated with shorter sequence lengths.

![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/cc9eda02-b9a0-4746-aa43-993181f35ccf)
Proteins with a lower denaturation temperature tend to have a higher occurrence of polar amino acids.


![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/59cca46c-d581-4072-a4d1-a22860668de8)
Proteins with a high denaturation temperature more often include hydrophobic amino acids.
![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/812de67b-2e26-4f64-9206-6243aa3afba4)
Proteins with higher denaturation temperatures are more frequently composed of amino acids with a smaller free surface area.







5. [eda_clusters.ipynb](./process_data/eda_clusters.ipynb) 


