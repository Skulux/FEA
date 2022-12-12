import configparser
import os
import time


def create():
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
            create()
            return "light", "de"
        return theme, lang
    except:
        create()
        return "light", "de"


def read():
    config = configparser.ConfigParser()
    config.read('config.ini')
    theme = config.get('GENERAL', 'theme')
    lang = config.get('GENERAL', 'language')
    return theme, lang


def change(theme=None, language=None):
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        if theme:
            theme = config.set('GENERAL', 'theme', theme)
        if language:
            lang = config.set('GENERAL', 'language', language)
        if theme or language:
            with open(r"config.ini", "w") as configfile:
                config.write(configfile)
        theme = config.get('GENERAL', 'theme')
        lang = config.get('GENERAL', 'language')
        return theme, lang
    except Exception as ERR:
        print(ERR)


print(change(language="de"))
