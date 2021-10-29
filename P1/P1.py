from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def myAES(key, m):
    if len(m) != 16:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(m) + encryptor.finalize()
    return ct

# encrypt Tux.body with your ECB implementation, save the encrypted file as Tux.body.ecb
with open('Tux.body', 'rb') as f:
    body = f.read()
    # Encrypt Tux.body 16 by 16 bytes
    for i in range(0, len(body), 16):
        ct = myAES(b'YELLOW SUBMARINE', body[i:i+16])
        with open('Tux.body.ecb', 'ab') as f:
            f.write(ct)
