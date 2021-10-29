from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def get_gcm_cipher(key: str):
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.GCM(), backend=default_backend())
    return cipher

def encrypt(key, m):
    cipher = get_gcm_cipher(key)
    encryptor = cipher.encryptor()
    ct = encryptor.update(m) + encryptor.finalize()
    return ct

def decrypt(key, ct):
    cipher = get_gcm_cipher(key)
    decryptor = cipher.decryptor()
    m = decryptor.update(ct) + decryptor.finalize()
    return m

with open('Tux.body', 'rb') as f:
    body = f.read() 
    ct = encrypt(b'YELLOW SUBMARINE', body)
    with open('Tux.body.gcm', 'wb') as f:
        f.write(ct)
    dec = decrypt(b'YELLOW SUBMARINE', ct)
    with open('Tux.boby.gcm.dec', 'wb') as f:
        f.write(dec)