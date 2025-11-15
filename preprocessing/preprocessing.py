# preprocessing/preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from .normalization import min_max_normalize

def load_and_preprocess():
    df = pd.read_csv("data/parkinsons.csv")

    df = df.dropna()
    
    X = df.drop("status", axis=1)
    y = df["status"]

    X = min_max_normalize(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    return X_train.values, X_test.values, y_train.values, y_test.values
