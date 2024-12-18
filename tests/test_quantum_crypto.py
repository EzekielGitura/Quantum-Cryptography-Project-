import unittest
from src.quantum_crypto_system import QuantumCryptographySystem

class TestQuantumCryptoSystem(unittest.TestCase):
    def setUp(self):
        self.qcs = QuantumCryptographySystem()
    
    def test_key_distribution(self):
        result = self.qcs.quantum_key_distribution()
        
        self.assertIsNotNone(result['key'])
        self.assertEqual(result['security_level'], 'HIGH')
    
    def test_encryption_decryption(self):
        original_message = b"Quantum cryptography is amazing!"
        encrypted_message = self.qcs.encrypt_message(original_message)
        
        quantum_key = self.qcs.quantum_key_distribution()['key']
        decrypted_message = self.qcs.decrypt_message(encrypted_message, quantum_key)
        
        self.assertEqual(original_message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
