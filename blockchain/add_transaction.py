# blockchain/add_transaction.py
from .blockchain import Blockchain

bc = Blockchain()

# Example usage
bc.add_transaction(client_id=1, weights=[0.1, 0.2, 0.3])
