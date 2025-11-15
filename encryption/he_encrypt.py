# encryption/he_encrypt.py
import numpy as np

def encrypt(weights, public_key=1234567):
    noise = np.random.normal(0, 0.001, size=len(weights))
    return weights + noise

def decrypt(encrypted_weights):
    return encrypted_weights
