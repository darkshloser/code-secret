import os
import sys
from config import Configuration
from crypto import Crypto


class Actions(object):
    def __init__(self):
        self.config = Configuration()
        import pdb;
        pdb.set_trace()
        test = Crypto()

    def indirect(self,option_name, args):
        method_name='_'+str(option_name)
        method=getattr(self, method_name, lambda : 'Invalid')
        return method(args)

    def _is_git_repo(self, location):
        cmd = 'git -C {path} rev-parse 2> /dev/null > /dev/null'.format(path=location)
        if os.system(cmd) == 0:
            return True
        else:
            return False

    def get_git_root(self, location='.'):
        def inner_termination():
            root_location = None
            root_found = None
        if not self._is_git_repo(location):
            print("There is no git repository!")
            sys.exit(1)

        root_location = location
        root_found = False
        try:
            while root_found == False:
                dirs = next(os.walk(root_location))[1]
                if self.config.get_default['git_dir'] in dirs:
                    root_found = True
                else:
                    root_location = os.path.join(root_location, '..')
            inner_termination()
            return root_location
        except:
            inner_termination()
            print("There is no git repository!")
            sys.exit(1)

    @property
    def get_secret_dir(self):
        root_dir = self.get_git_root()
        git_dir = os.path.join(root_dir, self.config.get_default['git_dir'])
        secret_dir = os.path.join(git_dir, self.config.get_default['secret_dir'])
        return secret_dir

    def _init(self, path):
        #Check if path was given
        if len(path) >= 2:
            print("More than one path given!")
            sys.exit(1)
        elif not len(path):
            path = ['.']
        path = path[0]

        #Check if the given path is valid
        if not os.path.isdir(path):
            print('Given path %s is not a valid one!' % (path))
            sys.exit(1)

        #Get the root dir of the repository
        root_dir = self.get_git_root(path)

        #Check if '.secret' already exists
        git_dir = os.path.join(root_dir, self.config.get_default['git_dir'])
        secret_dir = os.path.join(git_dir, self.config.get_default['secret_dir'])
        if not os.path.isdir(secret_dir):
            try:
                os.mkdir(secret_dir)
            except OSError:
                print("Creation of the directory %s failed!" % (secret_dir))
                sys.exit(1)

        #Check the list for encryption
        encryption_list_location = \
            os.path.join(secret_dir, self.config.get_specific['encryption_list'])
        if not os.path.isfile(encryption_list_location):
            try:
                _ = open(encryption_list_location, "x")
                print('Initialization of code-secret was successfully executed!')
            except:
                pass
        else:
            print('Initialization was already performed!')
        sys.exit(0)

    def _add(self, args):
        secret_dir = self.get_secret_dir
        encryption_list_location = \
            os.path.join(secret_dir, self.config.get_specific['encryption_list'])

        if not os.path.isfile(encryption_list_location):
            print("Code-secret initialization wasn't performed!")
            sys.exit(1)

        if not isinstance(args, list) or isinstance(args, list) \
            and len(args) == 0:
            print("No files to add for encryption!")
            sys.exit(1)

        for file in args:
            if not os.path.isfile(file):
                print("Given file name(s) doesn't exist!")
                sys.exit(1)

        file_to_add = []
        with open(encryption_list_location, 'r') as encrytFiles:
            for line in encrytFiles:
                if not any(file_to_encript in line for file_to_encript in args):
                    file_to_add.append(os.path.abspath(file_to_encript))

        with open(encryption_list_location, 'a+') as fileObject:
            for item in file_to_add:
                fileObject.write("\n")
                fileObject.write(item)

    def _remove(self, args):
        print("REMOVE")

    def _terminate(self, args):
        print("TERMINATE")
