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
1. [wget_filter.ipynb](./process_data/wget_filter.ipynb): Obtaining preprocessed mass spectrometry-based data encompassing melting temperatures of 34,925 proteins from 13 model organisms. [Article](https://www.nature.com/articles/s41592-020-0801-4 )

To ensure data quality, duplicates were eliminated. Additionally, proteins longer than 1,020 amino acids were excluded as the transformer model has limitations on input sequence length.

3. [clustering.ipynb](./process_data/clustering.ipynb): The data has been categorized into three ordinal groups based on denaturation temperature. I have also calculated the statistical count for each category.

![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/3b596bbb-d509-49b2-bbcb-459bedea7206)

The majority of proteins in the dataset fall into the second category, characterized by a denaturation temperature ranging from 40 to 60 degrees.

3. [feature_distribution.ipynb](./process_data/feature_distribution.ipynb): We have computed the distributions of primary and tertiary structure features for proteins based on their ordinal category of denaturation temperature.



![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/4a46d603-fdee-488a-b87f-28dc10a92b06)

Proteins exhibiting higher denaturation temperatures are typically associated with shorter sequence lengths.

![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/cc9eda02-b9a0-4746-aa43-993181f35ccf)

Proteins with a lower denaturation temperature tend to have a higher occurrence of polar amino acids.

![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/59cca46c-d581-4072-a4d1-a22860668de8)

Proteins with a high denaturation temperature more often include hydrophobic amino acids.

![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/812de67b-2e26-4f64-9206-6243aa3afba4)

Proteins with higher denaturation temperatures are more frequently composed of amino acids with a smaller free surface area.



5. [eda_clusters.ipynb](./process_data/eda_clusters.ipynb): I have clustered evolutional clusters by aligning protein sequences with an identity threshold of 0.7. Subsequently, I calculated cumulative statistics regarding the number of clusters, considering the protein representation 	within each cluster.

   ![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/5553ff9f-b594-47ce-801d-339a82fdcfb9)

## Training model
[training.ipynb](./training/train_valid.ipynb)

TabNet, after undergoing numerous experiments, has consistently demonstrated superior performance compared to other models. This exceptional performance can be attributed to its unique attention mechanism, which empowers the model to effectively identify and leverage the most relevant features of the input data. By focusing on these crucial factors, TabNet enhances its predictive capabilities, resulting in significantly more accurate predictions.

![image](https://github.com/GavrilenkoA/Tm_prediction/assets/92908421/f8b6ff7e-fbe8-4aa5-86e5-4f85cfcf26d0)

The regression model training process involved multiple essential steps:
1. Hyperparameter Selection: Optuna was utilized to carefully select the optimal hyperparameters for the model. This thorough optimization process aids in maximizing the model's performance by fine-tuning key parameters.

2. Dataset Splitting: The training and validation samples were split using the train_test_split technique. This separation allows for evaluating the model's performance on unseen data and helps prevent overfitting.

3. Hyperparameter Fine-Tuning: Once the best-performing hyperparameters were determined, they were fixed to ensure consistent and optimal model quality throughout the training process.

4. Cross-Validation: To account for evolutionary similarity and denaturation temperature of proteins, a cross-validation approach was employed. The dataset was partitioned, and a family of models was trained on each partition. This methodology helps capture the inherent variations within the data and enhances the model's robustness.

5. Metric Calculation: Metrics were calculated based on the validation and test samples to assess the performance of the trained models. These metrics provide valuable insights into how well the models generalize to unseen data and inform decisions regarding model selection and optimization.





