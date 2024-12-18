import os
from typing import Dict, Any
from cryptography.hazmat.primitives.asymmetric import rsa
from quantum_random import get_random_bytes

class KeyManager:
    def __init__(self, key_length: int = 2048):
        """
        Initialize key management system.
        
        Args:
            key_length (int): RSA key length
        """
        self.key_length = key_length
        self.key_registry: Dict[str, Any] = {}
    
    def generate_quantum_key(self, circuit_counts: Dict) -> bytes:
        """
        Generate quantum random key based on circuit measurement.
        
        Args:
            circuit_counts (Dict): Quantum circuit measurement counts
        
        Returns:
            bytes: Quantum random key
        """
        # Use circuit counts as seed for randomness
        seed = hash(frozenset(circuit_counts.items()))
        os.urandom(seed)
        
        # Generate quantum random bytes
        quantum_key = get_random_bytes(32)
        
        return quantum_key
    
    def generate_rsa_key_pair(self) -> Dict[str, Any]:
        """
        Generate RSA key pair.
        
        Returns:
            Dict containing private and public keys
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_length
        )
        public_key = private_key.public_key()
        
        return {
            'private_key': private_key,
            'public_key': public_key
        }
    
    def rotate_keys(self) -> Dict[str, Any]:
        """
        Rotate cryptographic keys.
        
        Returns:
            Dict with new key pair
        """
        new_key_pair = self.generate_rsa_key_pair()
        key_id = os.urandom(16).hex()
        
        self.key_registry[key_id] = {
            **new_key_pair,
            'created_at': os.time()
        }
        
        return {
            'key_id': key_id,
            **new_key_pair
        }
