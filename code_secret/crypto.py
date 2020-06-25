import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Crypto(object):
    def __init__(self):
        self.key_path = password = input("Set full key path: ")
        if self.key_path.length > 0:
            if os.path.dirname(self.key_path):
                return

        raise Exception("You need to specify path to existing " + \
            "key or full path to the newly generated one!")

    @property
    def is_key_created(self):
        if self.key_path.length > 0 and os.path.isfile(self.key_path):
            try:
                with open(self.key_path, "rb") as key_file:
                    _ = serialization.load_pem_private_key(
                        key_file.read(),
                        password=None,
                        backend=default_backend()
                    )
                return True
            except:
                pass

        return False

    @property
    def create_key(self):
        if not self.is_key_created:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
        else:
            private_key = self.get_key
        return private_key

    @property
    def get_public_key(self):
        if self.is_key_created:
            return self.get_key.public_key()
        return None

    @property
    def get_key(self):
        if self.is_key_created:
            try:
                with open(self.key_path, "rb") as key_file:
                    return serialization.load_pem_private_key(
                        key_file.read(),
                        password=None,
                        backend=default_backend()
                    )
            except:
                pass
        return None
