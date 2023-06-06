from eveparser.parsers.base import UnTabbedParser
from eveparser.converters import normalize_string, to_int
from eveparser.errors import ParserError
from eveparser.validators import is_int


class NameSpaceQuantity(UnTabbedParser):
    """Ragnarok 2"""

    @classmethod
    def parse(cls, string: str) -> tuple[str, int]:
        super().parse(string)
        if " " not in string:
            raise ParserError("Required space missing")
        parts = string.split(" ")

        quantity_str = parts[-1]
        if not is_int(quantity_str):
            raise ParserError("Quantity is not int")
        quantity = to_int(quantity_str)

        name_raw = " ".join(parts[:-1])
        name = normalize_string(name_raw)
        return name, quantity