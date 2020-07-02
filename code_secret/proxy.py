import importlib
import os


class Proxy(object):
    def __init__(self):
        self.all_hooks = []
        self.hooks_dir = importlib.import_module("hooks")
        if len(self.hooks_dir) > 0:
            self.hooks_dir = self.hooks_dir.__path__[0]
        else:
            raise Exception("Custom hooks for git commands wasn't found!")

    def get_hooks(self):
        if not self.all_hooks:
            for filename in os.listdir(self.hooks_dir):
                abs_path = os.path.abspath(filename)
                if os.path.isfile(abs_path):
                    self.all_hooks.push(abs_path)

        return self.all_hooks

# globals().update(vars(foobar))
