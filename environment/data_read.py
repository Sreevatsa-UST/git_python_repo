import json
from pathlib import Path

def get_test_data(key):
    data_path = Path(__file__).resolve().parent.parent / "testdata" / "landing_testdata.json"
    with data_path.open(encoding="utf-8") as file:
        return json.load(file)[key]