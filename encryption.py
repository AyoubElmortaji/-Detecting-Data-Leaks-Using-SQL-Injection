from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
from os import urandom

KEY = urandom(32)

def encrypt(plain_text: str) -> str:
    iv = urandom(16)
    cipher = Cipher(algorithms.AES(KEY), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(plain_text.encode()) + encryptor.finalize()
    return b64encode(iv + encrypted).decode()

def decrypt(encrypted_text: str) -> str:
    data = b64decode(encrypted_text)
    iv = data[:16]
    ct = data[16:]
    cipher = Cipher(algorithms.AES(KEY), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ct) + decryptor.finalize()).decode()
