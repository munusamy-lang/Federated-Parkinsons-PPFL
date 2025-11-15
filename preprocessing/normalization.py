# preprocessing/normalization.py
import pandas as pd

def min_max_normalize(df: pd.DataFrame):
    return (df - df.min()) / (df.max() - df.min())
