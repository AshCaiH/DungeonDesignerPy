import Grid
import json
from ast import literal_eval

def save_file():
    file = open("levels/map1.dun", "w+")

    export_data = {
        "elements": Grid.elements_dict,
        "cells": {str(key): value for key, value in Grid.cell_dict.items()}
    }

    json.dump(export_data, file)

    print("Saved")


def load_file():
    print("Loading...")

    loaded = json.load(open("levels/map1.dun", "r"))["cells"]



    loaded = {literal_eval(key): value for key, value in loaded.items()}

    Grid.cell_dict = loaded