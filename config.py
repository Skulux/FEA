import configparser
import os
import time
import json
directory = os.path.dirname(os.path.realpath(__file__))

def create():
    """
    creates a configfile and deletes old one.
    :return:
    """
    config = configparser.ConfigParser()
    if os.path.isfile(f'{directory}\\config.ini'):
        os.remove(f'{directory}\\config.ini')
    config.add_section('GENERAL')
    config.set('GENERAL', 'language', 'en-US')
    config.set('GENERAL', 'theme', 'light')
    with open(rf"{directory}\\config.ini", "w") as configfile:
        config.write(configfile)


def setup():
    """
    sets up the config, if config not available creates new one
    :return: tuple(str, str) theme, language
    """
    config = configparser.ConfigParser()
    try:
        config.read(f'{directory}\\config.ini')
        theme = config.get('GENERAL', 'theme')
        lang = config.get('GENERAL', 'language')
        if theme not in ['dark', 'light']:
            create()
            return "light", "en-US"
        return theme, lang
    except:
        create()
        return "light", "en-US"


def read():
    """
    reads the config
    :return: tuple(str, str) theme and language
    """
    config = configparser.ConfigParser()
    config.read(f'{directory}\\config.ini')
    theme = config.get('GENERAL', 'theme')
    lang = config.get('GENERAL', 'language')
    return theme, lang


def change(theme=None, language=None):
    """
    changes theme and/or language if given in the config
    :param theme: string dark/light
    :param language: string de-DE/en-US
    :return: tuple(str, str) theme and lang
    """
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
    """
    loads the language file (lang.json)
    :return:
    """
    return json.load(open(f"{directory}\\lang.json"), encoding='utf-8')

