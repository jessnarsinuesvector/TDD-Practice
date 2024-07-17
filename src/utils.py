import json


def load_numeral_map(map_file_path: str) -> dict:
    try:
        with open(map_file_path) as f:
            return json.loads(f.read())
    except Exception as e:
        raise Exception("Cannot load roman numeral map! {}".format(map_file_path))
