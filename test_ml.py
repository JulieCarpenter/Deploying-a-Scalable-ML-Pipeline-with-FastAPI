import os
from numpy import load
import pytest
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import load_model, train_model

# Define variables
project_path = "../Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
data_path = os.path.join(project_path, "data", "census.csv")
data = pd.read_csv(data_path)
train, test = train_test_split(data, test_size=0.20)

# Tests
def test_model_exists():
    """
    # Confirm that the model was created
    """
    model = load_model(os.path.join(project_path, "model", "model.pkl"))
    assert type(model) == sklearn.ensemble._forest.RandomForestClassifier

def test_num_train_rows():
    """
    # Confirm that number of rows in training set are as expected
    """
    assert train.shape[0] == 26048

def test_num_test_rows():
    """
    # Confirm that number of rows in test set are as expected
    """
    assert test.shape[0] == 6513
