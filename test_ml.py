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

def test_num_rows():
    """
    # Confirm that number of rows in training and test sets are as expected
    """
    assert train.shape[0] == 26048
    assert test.shape[0] == 6513

def test_pickles():
    """
    # Confirm that pickle files were created
    """
    pickle_enc = os.path.join(project_path, "model", "encoder.pkl")
    pickle_mod = os.path.join(project_path, "model", "model.pkl")
    assert os.path.exists(pickle_enc)
    assert os.path.exists(pickle_mod)
   
    
