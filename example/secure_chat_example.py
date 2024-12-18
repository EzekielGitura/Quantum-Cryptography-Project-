from src.quantum_crypto_system import QuantumCryptographySystem

def simulate_secure_chat():
    # Initialize quantum cryptography system
    qcs = QuantumCryptographySystem()
    
    # Simulate message exchange
    alice_message = b"Hello, quantum-secure world!"
    
    # Alice encrypts the message
    encrypted_message = qcs.encrypt_message(alice_message)
    
    # Bob receives and decrypts the message
    quantum_key = qcs.quantum_key_distribution()['key']
    decrypted_message = qcs.decrypt_message(encrypted_message, quantum_key)
    
    print("Original Message:", alice_message)
    print("Decrypted Message:", decrypted_message)
    
    assert alice_message == decrypted_message, "Message transmission failed!"

if __name__ == "__main__":
    simulate_secure_chat()
