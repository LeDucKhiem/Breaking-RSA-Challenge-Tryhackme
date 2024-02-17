from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Path to your id_rsa.pub file
public_key_path = 'id_rsa.pub'

# Function to extract the modulus (n component) from the RSA public key
def extract_modulus(public_key_path):
    with open(public_key_path, 'rb') as f:
        # Load the RSA public key
        public_key = serialization.load_ssh_public_key(
            f.read(),
            backend=default_backend()
        )
    
    # Get the modulus (n component)
    modulus = public_key.public_numbers().n
    
    return modulus

# Extract the modulus (n component)
modulus = extract_modulus(public_key_path)
print("Modulus (n component):", modulus)
