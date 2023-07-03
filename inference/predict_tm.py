#!/usr/bin/env


import torch
import numpy as np
import glob
import os
from extract import calculate_emb, create_parser

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

embed_pattern = './inference/embed/*.pt'
model_pattern = './model/*.pt'

parser = create_parser()
args = parser.parse_args()


def concat_models(model_pattern: str = model_pattern) -> list:
    all_models = []
    path_models = glob.glob(model_pattern)
    for path in path_models:
        model = torch.load(path)
        all_models.append(model)
    return all_models


def average_predict(x: np.array, all_models: list) -> float:
    all_pred = []
    for model in all_models:
        pred = model.predict(x)
        all_pred.append(pred)

    all_pred = np.concatenate(all_pred, axis=1)
    tm = all_pred.mean(axis=1)[0]
    return tm


def process_tensor(embed_pattern: str = embed_pattern) -> tuple[list[float], list[str]]:
    pt_files = glob.glob(embed_pattern)

    labels = []
    melt_temperatures = []
    all_models = concat_models()

    for file in pt_files:
        entry = torch.load(file)
        embed = entry['mean_representations'][33].reshape(1, -1).numpy()
        label = entry['label']
        tm = average_predict(embed, all_models)
        labels.append(label)
        melt_temperatures.append(tm)
    return melt_temperatures, labels


def clean_embed(embed_pattern: str = embed_pattern) -> None:
    pt_files = glob.glob(embed_pattern)

    for file in pt_files:
        os.remove(file)


def print_file(melt_temperatures: list[float], labels: list[str]) -> None:
    with open('tm_prediction.txt', 'w') as fi:
        for id_, tm in zip(labels, melt_temperatures):
            fi.write(id_)
            fi.write('\n')
            fi.write(str(tm))
            fi.write('\n')


def main():
    calculate_emb(args)
    melt_temperatures, labels = process_tensor()
    print_file(melt_temperatures, labels)
    clean_embed()


if __name__ == "__main__":
    main()
