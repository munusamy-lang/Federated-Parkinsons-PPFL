# federated_learning/fedavg.py
import numpy as np

def fed_avg(weight_list):
    return np.mean(weight_list, axis=0)
