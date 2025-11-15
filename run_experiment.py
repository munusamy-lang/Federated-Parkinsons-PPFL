# run_experiment.py
from preprocessing.preprocessing import load_and_preprocess
from federated_learning.server import FederatedServer
from federated_learning.client import FederatedClient
import json

def main():
    # Load config
    with open("federated_learning/config.json", "r") as f:
        config = json.load(f)

    print("Loading and preprocessing dataset...")
    X_train, X_test, y_train, y_test = load_and_preprocess()

    # Create server
    server = FederatedServer(config)

    # Create clients
    clients = []
    num_clients = config["num_clients"]
    data_per_client = len(X_train) // num_clients

    for i in range(num_clients):
        start = i * data_per_client
        end = (i + 1) * data_per_client
        client = FederatedClient(
            client_id=i,
            X=X_train[start:end],
            y=y_train[start:end],
            config=config
        )
        clients.append(client)

    print("Starting federated learning rounds...")
    for rnd in range(config["global_rounds"]):
        print(f"\n--- Round {rnd+1}/{config['global_rounds']} ---")

        local_updates = []
        for client in clients:
            w = client.train_local_model()
            local_updates.append(w)

        server.aggregate(local_updates)

    print("\nTraining complete!")

if __name__ == "__main__":
    main()
