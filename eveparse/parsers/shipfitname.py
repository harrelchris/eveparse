from eveparse.parsers.base import UnTabbedParser
from eveparse.converters import to_int
from eveparse.errors import ParserError
from eveparse.validators import is_int


class ShipFitName(UnTabbedParser):
    """[Ragnarok, Bob's Ragnarok]"""

    @classmethod
    def parse(cls, string: str) -> tuple[str, int]:
        super().parse(string)
        if not string.startswith("["):
            raise ParserError("Required [ missing")
        if not string.endswith("]"):
            raise ParserError("Required ] missing")
        if ", " not in string:
            raise ParserError("Required comma space missing")

        parts = string.split(", ")

        name = parts[0]
        name = name.lstrip("[")
        return name, 1