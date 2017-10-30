import base64
import os

from Crypto.Cipher import XOR

class Crypter(object):
    def __init__(self, filename, out_path='out'):
        self.in_filename = filename
        self.out_filename = os.path.join(
            out_path,
            *self.in_filename.split(os.path.sep)[1:]
        )
        # for remove the first dir from path for maintaining same
        # hierarchy while encryption and decryption
        print(self.in_filename, self.out_filename)
        self.key = os.environ['cipher_key']
        self.cipher = XOR.new(self.key)
        self.file_data = self.readfile()


    def readfile(self):
        with open(self.in_filename) as file:
            data = file.read()
        return data

    def writefile(self, filepath, data):
        # if file path don exist createone
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))

        with open(filepath, "w") as file:
            status = file.write(data)
        return status

    def encode_b64(self, data):
        return base64.b64encode(data)

    def decode_b64(self, data):
        return base64.b64decode(data)

    def encrypt(self):
        return self.encode_b64(self.cipher.encrypt(self.file_data))

    def decrypt(self):
        return self.cipher.decrypt(self.decode_b64(self.file_data))

    def run_encryption(self):
        self.writefile(self.out_filename, self.encrypt())

    def run_decryption(self):
        self.writefile(self.out_filename, self.decrypt())

