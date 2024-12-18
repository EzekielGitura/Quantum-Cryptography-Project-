from src.quantum_crypto_system import QuantumCryptographySystem

def demonstrate_key_distribution():
    # Initialize quantum cryptography system
    qcs = QuantumCryptographySystem()
    
    # Perform quantum key distribution
    key_dist_result = qcs.quantum_key_distribution()
    
    print("Quantum Key Distribution Results:")
    print("Key Generated:", key_dist_result['key'].hex())
    print("Circuit Statistics:", key_dist_result['circuit_stats'])
    print("Security Level:", key_dist_result['security_level'])

if __name__ == "__main__":
    demonstrate_key_distribution()
