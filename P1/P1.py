from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import sys

def myAES(key: bytes, m: bytes):
    if len(m) != 16:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(m) + encryptor.finalize()
    return ct

def myAES_decrypt(key: bytes, ct: bytes):
    if len(ct) != 16:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct) + decryptor.finalize()
    return pt

def gen_key():
    key = os.urandom(16)
    print(key)
    return key

def encrypt(message: bytes, key: bytes):
    if len(message) % 16 != 0:
        # Pad key to 16 bytes
        message += b'\x00' * (16 - len(key) % 16)
    ct = b''
    for i in range(0, len(message), 16):
        ct += myAES(key, message[i:i+16])
    return ct

def decrypt(ciphertext: bytes, key: bytes):
    pt = b''
    for i in range(0, len(ciphertext), 16):
        pt += myAES(key, ciphertext[i:i+16])
    return pt

def main():
    if len(sys.argv) != 2:
        exit(1)
    body_filename = sys.argv[1]
    key = gen_key()
    with open(body_filename, 'rb') as f:
        body = f.read()
        ct = encrypt(body, key)
        with open(body_filename + '.enc', 'wb') as f:
            f.write(ct)
        pt = decrypt(ct, key)
        with open(body_filename + '.dec', 'wb') as f:
            f.write(pt)


if __name__ == '__main__':
    main()