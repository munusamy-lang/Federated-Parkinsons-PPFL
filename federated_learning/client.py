# federated_learning/client.py
import numpy as np

class FederatedClient:
    def __init__(self, client_id, X, y, config):
        self.client_id = client_id
        self.X = X
        self.y = y
        self.config = config
        self.weights = np.zeros(X.shape[1])

    def train_local_model(self):
        lr = self.config["learning_rate"]
        epochs = self.config["local_epochs"]

        for _ in range(epochs):
            preds = np.dot(self.X, self.weights)
            error = self.y - preds
            gradient = -2 * np.dot(self.X.T, error) / len(self.X)
            self.weights -= lr * gradient

        print(f"Client {self.client_id} finished training.")
        return self.weights
