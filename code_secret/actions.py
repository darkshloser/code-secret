import os


class Actions(object):
    def indirect(self,option_name, args):
        method_name='_'+str(option_name)
        method=getattr(self, method_name, lambda : 'Invalid')
        return method(args)

    def _init(self, path):
        #Check if path was given
        if len(path) >= 2:
            raise ValueError('More than one path given!')
        elif not len(path):
            path = ['.']

        #Check if the given path is valid
        if not os.path.isdir(path[0]):
            raise ValueError('Given path %s is not a valid one!' % (path[0]))



    def _add(self, args):
        print("ADD")

    def _remove(self, args):
        print("REMOVE")

    def _terminate(self, args):
        print("TERMINATE")
