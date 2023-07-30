import json
import os

CONFIG_PATH = '/config.json'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def config():
    """
    returns calculator button coordinate dictionary
    """
    with open(DIR_PATH + CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


