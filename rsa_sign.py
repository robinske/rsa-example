import argparse
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature


parser = argparse.ArgumentParser()
parser.add_argument('message')
args = parser.parse_args()

message = str.encode(args.message)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

print("Signing message: '{}'\n".format(args.message))
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(
            hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Signature: \n{}\n".format(signature))

public_key = private_key.public_key()

try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(
                hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Successfully validated signature.")
except InvalidSignature as e:
    print("Could not validate signature.")
