# src/utils.py
import logging
import qiskit
import numpy as np
from qiskit import QuantumCircuit

def generate_quantum_noise(qc: QuantumCircuit) -> QuantumCircuit:
    """
    Add simulated quantum noise to circuit.
    
    Args:
        qc (QuantumCircuit): Input quantum circuit
    
    Returns:
        QuantumCircuit: Circuit with added noise
    """
    # Depolarizing noise
    noise_prob = 0.01
    for qubit in range(qc.num_qubits):
        if np.random.random() < noise_prob:
            qc.depolarizing_error(noise_prob, qubit)
    
    return qc

def log_security_event(event: str, status: str) -> None:
    """
    Log security-related events.
    
    Args:
        event (str): Description of security event
        status (str): Event status (SUCCESS/FAILURE)
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - QUANTUM_SECURITY - %(levelname)s: %(message)s'
    )
    
    logger = logging.getLogger('QuantumSecurity')
    
    if status == 'SUCCESS':
        logger.info(f"Security Event: {event}")
    else:
        logger.warning(f"Security Event: {event}")

def validate_quantum_measurement(measurement: dict) -> bool:
    """
    Validate quantum circuit measurement results.
    
    Args:
        measurement (dict): Measurement results from quantum circuit
    
    Returns:
        bool: Validation result
    """
    # Implement advanced quantum measurement validation
    total_shots = sum(measurement.values())
    dominant_state_percentage = max(measurement.values()) / total_shots
    
    return dominant_state_percentage > 0.8
