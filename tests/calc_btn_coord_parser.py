import json
import os

CONFIG_PATH = '/calculator_btn_coord.json'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def calc_btn_coord():
    """
    returns calculator button coordinate dictionary
    """
    with open(DIR_PATH + CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


