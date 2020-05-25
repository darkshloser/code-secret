import configparser


class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_dict(
            {'default': {'name': 'code-secret',
                         'version': '0.3',
                         'git_dir': '.git',
                         'secret_dir': '.secret'},
             'specific': {'encryption_list': 'encryption'}
            }
        )

    @property
    def get_sections(self):
        return self.config.sections()

    @property
    def get_default(self):
        return self.config['default']

    @property
    def get_specific(self):
        return self.config['specific']
