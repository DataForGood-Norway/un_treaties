from io import StringIO
import json

import pandas as pd

from un_treaties import resources

_CSV_STR = StringIO(resources.read_text("un_treaties.data", "un_treaties.csv"))
DATAFRAME = pd.read_csv(_CSV_STR)

_JSON_STR = resources.read_text("un_treaties.data", "un_treaties.json")
JSON = json.loads(_JSON_STR)


def as_dataframe():
    return DATAFRAME


def as_dict():
    return JSON
