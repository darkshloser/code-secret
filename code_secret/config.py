import configparser


class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_dict(
            {'default': {'name': 'code-secret',
                         'version': '0.3',
                         'git_dir': '.git'}
            }
        )

    @property
    def get_sections(self):
        return self.config.sections()

    @property
    def get_default(self):
        return self.config['default']
