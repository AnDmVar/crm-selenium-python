import configparser
from constants import paths

config = configparser.ConfigParser()
config.read(paths.CONFIG_DIR / 'config.ini')


def get_value(section, option):
    return config[section][option]


def get_values(section):
    return config[section]
