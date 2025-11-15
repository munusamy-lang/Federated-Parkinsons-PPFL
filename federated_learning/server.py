# federated_learning/server.py
import numpy as np
from .fedavg import fed_avg

class FederatedServer:
    def __init__(self, config):
        self.config = config
        self.global_weights = None

    def aggregate(self, updates):
        self.global_weights = fed_avg(updates)
        print("Aggregated global model:", self.global_weights[:5], "...")
