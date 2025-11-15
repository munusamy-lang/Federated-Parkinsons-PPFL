# blockchain/blockchain.py
import json
import time

class Blockchain:
    def __init__(self, ledger_path="blockchain/ledger.json"):
        self.ledger_path = ledger_path

    def add_transaction(self, client_id, weights):
        entry = {
            "client_id": client_id,
            "timestamp": time.time(),
            "weights_hash": str(hash(str(weights.tolist())))
        }

        with open(self.ledger_path, "r") as f:
            ledger = json.load(f)

        ledger.append(entry)

        with open(self.ledger_path, "w") as f:
            json.dump(ledger, f, indent=4)

        print(f"Transaction added for client {client_id}")
