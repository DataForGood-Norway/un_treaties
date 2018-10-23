from io import StringIO
import json

import pandas as pd

import un_treaties

# Cached data
_DATAFRAME = None
_JSON = None


def _read_dataframe():
    global _DATAFRAME
    if _DATAFRAME is None:
        csv_path = un_treaties.get_local_path("un_treaties.csv")
        if not csv_path.exists():
            raise FileNotFoundError("The CSV dataset does not exist. Try to run un_crawl")
        _DATAFRAME = pd.read_csv(csv_path)


def _read_json():
    global _JSON
    if _JSON is None:
        json_path = un_treaties.get_local_path("un_treaties.json")
        print(json_path)
        if not json_path.exists():
            raise FileNotFoundError("The JSON dataset does not exist. Try to run un_crawl")
        json_str = json_path.read_text()
        _JSON = json.loads(json_str)


def as_dataframe():
    _read_dataframe()
    return _DATAFRAME


def as_dict():
    _read_json()
    return _JSON
