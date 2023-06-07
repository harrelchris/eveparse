import functools
import json
import pathlib

INV_TYPES_JSON_FILE_PATH = str(pathlib.Path(__file__).parent / "data/invTypes.json")

with open(INV_TYPES_JSON_FILE_PATH, "r", encoding="utf-8") as json_file:
    inv_types_dict = json.load(json_file)
    TYPE_NAMES_MAP = map(str.casefold, inv_types_dict.keys())


def is_int(string: str) -> bool:
    # these patterns indicate a float value such as 1,000.00
    if "," in string and "." in string:
        return False
    if " " in string and "." in string:
        return False
    if " " in string and "," in string:
        return False

    # indicates a decimal less than 1 such as 0.5
    if string.startswith("0"):
        return False

    # numbers may be separated with period, comma, or space
    # https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html
    normalized = string.replace(" ", "").replace(",", "").replace(".", "")
    return normalized.isdigit()


def is_legal_string(string: str) -> bool:
    return True


@functools.lru_cache(maxsize=25000)  # slightly more than number of currently published invTypes at 23623
def is_valid_name(string: str) -> bool:
    return string in TYPE_NAMES_MAP
