import configparser


class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_dict(
            {'default': {'Name': 'code-secret',
                         'Version': '0.3'}
            }
        )

    @property
    def get_sections(self):
        return self.config.sections()

    @property
    def get_default(self):
        return self.config['default']
