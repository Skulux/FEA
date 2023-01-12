import configparser
import os
import json
directory = os.path.dirname(os.path.realpath(__file__))

def create():
    """
    creates a configfile and deletes old one.
    :return:
    """
    if os.path.isfile(f'{directory}\\config.ini'):
        os.remove(f'{directory}\\config.ini')
    config = configparser.ConfigParser()
    config.add_section('GENERAL')
    config.set('GENERAL', 'language', 'en-US')
    config.set('GENERAL', 'theme', 'light')
    config.set('GENERAL', 'nsfw', 'false')
    with open(f"{directory}\\config.ini", "w") as configfile:
        config.write(configfile)


def setup():
    """
    sets up the config, if config not available creates new one
    :return: tuple(str, str) theme, language
    """
    config = configparser.ConfigParser()
    try:
        theme, lang, nsfw = read()
        if theme not in ['dark', 'light']:
            create()
            return "light", "en-US", "false"
        return theme, lang, nsfw
    except:
        create()
        return "light", "en-US", "false"


def read():
    """
    reads the config
    :return: tuple(str, str) theme and language
    """
    config = configparser.ConfigParser()
    config.read(f'{directory}\\config.ini')
    theme = config.get('GENERAL', 'theme')
    lang = config.get('GENERAL', 'language')
    nsfw = config.get('GENERAL', 'nsfw')
    return theme, lang, nsfw


def change(theme=None, language=None, nsfw=None):
    """
    changes theme and/or language if given in the config
    :param theme: string dark/light
    :param language: string de-DE/en-US
    :param nsfw: string false/true
    :return: tuple(str, str, str) theme, lang and nsfw
    """
    config = configparser.ConfigParser()
    try:
        config.read(f'{directory}\\config.ini')
        if theme:
            config.set('GENERAL', 'theme', theme)
        if language:
            config.set('GENERAL', 'language', language)
        if nsfw:
            config.set('GENERAL', 'nsfw', nsfw)
        if theme or language or nsfw:
            with open(f"{directory}\\config.ini", "w") as configfile:
                config.write(configfile)
        return read()
    except Exception as ERR:
        print(ERR)


def load_lang():
    """
    loads the language file (lang.json)
    :return:
    """
    return json.load(open(f"{directory}\\lang.json"))

