import configparser
import os
import time
import json
directory = os.path.dirname(os.path.realpath(__file__))

def create():
    config = configparser.ConfigParser()
    if os.path.isfile(f'{directory}\\config.ini'):
        os.remove(f'{directory}\\config.ini')
    config.add_section('GENERAL')
    config.set('GENERAL', 'language', 'de')
    config.set('GENERAL', 'theme', 'light')
    with open(rf"{directory}\\config.ini", "w") as configfile:
        config.write(configfile)


def setup():
    config = configparser.ConfigParser()
    try:
        config.read(f'{directory}\\config.ini')
        theme = config.get('GENERAL', 'theme')
        lang = config.get('GENERAL', 'language')
        if theme not in ['dark', 'light']:
            create()
            return "light", "de-DE"
        return theme, lang
    except:
        create()
        return "light", "de-DE"


def read():
    config = configparser.ConfigParser()
    config.read(f'{directory}\\config.ini')
    theme = config.get('GENERAL', 'theme')
    lang = config.get('GENERAL', 'language')
    return theme, lang


def change(theme=None, language=None):
    config = configparser.ConfigParser()
    try:
        config.read(f'{directory}\\config.ini')
        if theme:
            theme = config.set('GENERAL', 'theme', theme)
        if language:
            lang = config.set('GENERAL', 'language', language)
        if theme or language:
            with open(rf"{directory}\\config.ini", "w") as configfile:
                config.write(configfile)
        theme = config.get('GENERAL', 'theme')
        lang = config.get('GENERAL', 'language')
        return theme, lang
    except Exception as ERR:
        print(ERR)


def load_lang():
    return json.load(open(f"{directory}\\lang.json"), encoding='utf-8')

