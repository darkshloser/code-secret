import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Crypto(object):
    def __init__(self):
        self.key_path = raw_input("Set full key path: ")
        self.tmp_extention = ".temp"
        ## Check the given argument (path to the file where is the key or
        ## where it will be created)
        if len(self.key_path) > 0:
            try:
                if os.path.isdir(os.path.dirname(self.key_path)):
                    abs_base_path = \
                        os.path.abspath(os.path.dirname(self.key_path))
                    file_name = os.path.basename(self.key_path)
                    self.key_path = \
                        os.path.join(abs_base_path, file_name)
                    return
            except:
                pass

        raise Exception("You need to specify path to existing " + \
            "key or full path to the newly generated one!")

    @property
    def is_key_created(self):
        if len(self.key_path) > 0 and os.path.isfile(self.key_path):
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
        private_key = None
        if not self.is_key_created:
            try:
                private_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=2048,
                    backend=default_backend()
                )
                pem = private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
                with open(self.key_path, 'wb') as f:
                    f.write(pem)
            except:
                pass
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

    def _store_encription_data(self, file_path, encrypted_data):
        ''' Prepare backout copy for every file which is going to be
            encrypted and store encrypted info into files which will be commited
            to the repository.
        '''
        result = None
        if os.path.isfile(file_path):
            try:
                name = os.path.basename(file_path)
                path = os.path.dirname(file_path)
                temp_name = f"{name}{self.tmp_extention}"
                os.rename(os.path.join(path, name), \
                    os.path.join(path, temp_name))
                f = open(file_path, 'wb')
                f.write(encrypted_data)
                f.close()
                result = True
            except:
                pass
        return result

    def encrypt_file(self, files):
        ''' Encrypts all the files with absolute paths given in a list.
        '''
        result = None
        if self.is_key_created and self.get_public_key:
            result = True
            if not isinstance(fies, list):
                files = [].push(files)
            for item in files:
                if os.path.isfile(item):
                    f = open(item, 'rb')
                    message = f.read()
                    public_key = self.get_public_key
                    encrypted = public_key.encrypt(
                        message,
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )
                    if not self._store_encription_data(item, encrypted):
                        raise Exception(f"Error when storing encrypted data fot {item}")

        elif not self.is_key_created:
            print("The key is not created!")
        elif not self.get_public_key:
            print("Public key is NOT available!")
        return result
