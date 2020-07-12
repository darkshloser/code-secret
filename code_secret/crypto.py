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
        """
        This method will create RSA key if it doesn't exist
        on the pointed locationself.
        return : Private key (ready for usage)
        """
        private_key = None
        if not self.is_key_created:
            try:
                private_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=4096,
                    backend=default_backend()
                )
                pem = private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
                with open(self.key_path, 'wb') as f:
                    f.write(pem)
            except Exception as err:
                print("Something went wrong during key generation: "+ str(err))
                private_key = None
        else:
            private_key = self.get_key
        return private_key

    @property
    def get_public_key(self):
        """
        This method will retrieve the public key for data encryption.
        return : Public key (or 'None' if there is no key)
        """
        if self.is_key_created:
            return self.get_key.public_key()
        return None

    @property
    def get_key(self):
        """
        Will check if there ia s key already generated and it
        will return the content of it.
        return : Private key ('None' if doesn't exist)
        """
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
                temp_name = "{name}{ext}".format(name=name, ext=self.tmp_extention)
                os.rename(os.path.join(path, name), \
                    os.path.join(path, temp_name))
                f = open(file_path, 'wb')
                f.write(encrypted_data)
                f.close()
                result = True
            except:
                pass
        return result

    def _check_list_for_encryption(self, files):
        """
        Check all the files stored with their absolute paths and
        stop if some of the paths are not correct.
        files (IN) : List of files for encryption
        return (OUT) : Boolean confirmation if all the files are present
        """
        if not len(files) > 0:
            return False

        for file in files:
            if not os.path.isfile(file):
                return False
        return True

    def encrypt_file(self, files):
        """
        Encrypts all the files with absolute paths given in a list.
        files (IN) : List of files (absolute paths) which will be ancrypted
        return : True/False if all the files are successfully encrypted
        """
        result = False
        if not isinstance(fies, list) and not isinstance(files, str):
            print("Given argument is neither List nor String!")
            sys.exit(1)
        if self.is_key_created and self.get_public_key:
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
                        raise Exception("Error when storing encrypted data fot {item}".format(item))

        elif not self.is_key_created:
            print("The key is not created!")
        elif not self.get_public_key:
            print("Public key is NOT available!")
        return result
