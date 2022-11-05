import configparser
import os
import time


def create_config():
    config = configparser.ConfigParser()
    if os.path.isfile('config.ini'):
        os.remove('config.ini')
    config.add_section('GENERAL')
    config.set('GENERAL', 'language', 'de')
    config.set('GENERAL', 'theme', 'light')
    with open(r"config.ini", "w") as configfile:
        config.write(configfile)


def setup():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        theme = config.get('GENERAL', 'theme')
        lang = config.get('GENERAL', 'language')
        if theme not in ['dark', 'light']:
            create_config()
            return "light", "de"
        return theme, lang
    except:
        create_config()
        return "light", "de"




print(setup())
