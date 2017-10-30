import os
from crypt import Crypter



# enc = Crypter('files','test.py')
# enc.run_encryption()

def encrypt():
    for root, dirs, files in os.walk("files"):
       for name in files:
            print(root, name)
            enc = Crypter(os.path.join(root, name))
            enc.run_encryption()


def decrypt():
    for root, dirs, files in os.walk("out"):
       for name in files:
            print(root, name)
            enc = Crypter(os.path.join(root, name), 'files')
            enc.run_decryption()
encrypt()
#decrypt()