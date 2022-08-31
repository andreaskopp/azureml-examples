# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""This module will load mlflow model and do prediction."""

import argparse
import os
import pickle
from pathlib import Path

from mlflow.sklearn import load_model

MODEL_NAME = "iris_model"

<<<<<<< HEAD
=======

>>>>>>> main
def init():
    print("Environment variables start ****")
    for key, val in os.environ.items():
        print(key, val)
    print("Environment variables end ****")

<<<<<<< HEAD
    parser = argparse.ArgumentParser(allow_abbrev=False, description="ParallelRunStep Agent")
=======
    parser = argparse.ArgumentParser(
        allow_abbrev=False, description="ParallelRunStep Agent"
    )
>>>>>>> main
    parser.add_argument("--model", type=str, default=0)
    args, _ = parser.parse_known_args()

    model_path = args.model + "/" + MODEL_NAME
    global iris_model

    iris_model = load_model(model_path)


def run(input_data):
<<<<<<< HEAD
    
=======

>>>>>>> main
    # input_data is a Pandas DataFrame for Tabular Data

    num_rows, num_cols = input_data.shape
    pred = iris_model.predict(input_data).reshape((num_rows, 1))

    # cleanup output
    result = input_data.drop(input_data.columns[4:], axis=1)
<<<<<<< HEAD
    result['variety'] = pred
=======
    result["variety"] = pred
>>>>>>> main

    return result
