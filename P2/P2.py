import os
import sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt(body, key, nonce):
    aesgcm = AESGCM(key)
    ct = aesgcm.encrypt(nonce, body, b'')
    return ct

def decrypt(ct, key, nonce):
    aesgcm = AESGCM(key)
    pt = aesgcm.decrypt(nonce, ct, b'')
    return pt

def main():
    if len(sys.argv) != 2:
        exit(1)
    body_filename = sys.argv[1]
    key = AESGCM.generate_key(bit_length=128)
    nonce = os.urandom(12)
    with open(body_filename, 'rb') as f:
        body = f.read()
        ct = encrypt(body, key, nonce)
        with open(body_filename + '.enc', 'wb') as f:
            f.write(ct)
        pt = decrypt(ct, key, nonce)
        with open(body_filename + '.dec', 'wb') as f:
            f.write(pt)


if __name__ == '__main__':
    main()