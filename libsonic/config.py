from configparser import ConfigParser
import os


def _load_settings():
    home = os.path.abspath(os.path.expanduser('~'))
    config_file = os.path.join(home, '.config', 'py-sonic.ini')
    settings = ConfigParser()
    try:
        settings.read(config_file)
    except IOError:
        raise IOError('Config file does not exist at ~/.config/py-sonic.ini.')
    return settings


settings = _load_settings()
