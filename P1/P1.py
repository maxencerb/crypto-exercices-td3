from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
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

def gen_key() -> bytes:
    key = os.urandom(16)
    return key

def encrypt(message: bytes, key: bytes):
    message = padd_bytes(message)
    ct = b''
    for i in range(0, len(message), 16):
        ct += myAES(key, message[i:i+16])
    return ct

def decrypt(ciphertext: bytes, key: bytes):
    pt = b''
    for i in range(0, len(ciphertext), 16):
        pt += myAES_decrypt(key, ciphertext[i:i+16])
    pt = unpadd_bytes(pt)
    return pt

def padd_bytes(b: bytes):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(b) + padder.finalize()
    return padded_data

def unpadd_bytes(b: bytes):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(b) + unpadder.finalize()
    return unpadded_data

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