import os
from config import Configuration


class Actions(object):
    def __init__(self):
        self.config = Configuration()

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

    def get_git_root(self, location):
        def inner_termination():
            root_location = None
            root_found = None
        if not self._is_git_repo(location):
            raise ValueError('There is no git repository!')

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
            raise ValueError('There is no git repository!')

    def _init(self, path):
        #Check if path was given
        if len(path) >= 2:
            raise ValueError('More than one path given!')
        elif not len(path):
            path = ['.']
        path = path[0]

        #Check if the given path is valid
        if not os.path.isdir(path):
            raise ValueError('Given path %s is not a valid one!' % (path))

        #Get the root dir of the repository
        root_dir = self.get_git_root(path)

        #Check if '.secret' already exists
        git_dir = os.path.join(root_dir, self.config.get_default['git_dir'])
        if os.path.isdir(git_dir):
            print("Git directory exists!!")
        #Initialize code-secret into '.git' repository
        print(root_dir)

        #
        # #Check if init points to the root dir of the repository
        # if not os.path.isdir(os.path.join(path,'.git')):
        #     raise ValueError('Given path is not the root dir of the repository!')



    def _add(self, args):
        print("ADD")

    def _remove(self, args):
        print("REMOVE")

    def _terminate(self, args):
        print("TERMINATE")
