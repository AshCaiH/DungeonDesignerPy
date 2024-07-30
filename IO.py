import Grid
import json
from ast import literal_eval

def save_file():
    print("Saving...")

    print(json.dumps({str(key): value for key, value in Grid.cell_dict.items()}))


def load_file():
    print("Loading...")

    loaded = json.loads('{"(5.0, 5.0)": {"floor": 1, "nwall": 1, "wwall": 1}, "(6.0, 5.0)": {"floor": 1, "nwall": 1}, "(6.0, 6.0)": {"floor": 1}, "(7.0, 6.0)": {"wwall": 1}, "(6.0, 7.0)": {"nwall": 1}}')

    loaded = {literal_eval(key): value for key, value in loaded.items()}

    Grid.cell_dict = loaded

    print(loaded)