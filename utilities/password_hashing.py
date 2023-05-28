# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


class Passwordencryption:

    def __init__(self, password):
        self.password = password

    def hashed_password(self):
        encryption_key = get_random_bytes(16)
        iv = get_random_bytes(16)

        # Create an AES cipher object with the encryption key and IV
        cipher = AES.new(encryption_key, AES.MODE_CBC, iv=iv)

        # Pad the password to the appropriate block size
        padded_password = pad(self.password.encode('utf-8'), AES.block_size)

        # Encrypt the padded password
        encrypted_password = cipher.encrypt(padded_password)
        return encrypted_password.hex()
