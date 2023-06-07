from .converters import normalize_string
from .errors import ConverterError, ParserError, ValidatorError
from .validators import is_int, is_legal_string, is_valid_name

from .parsers.nameonly import NameOnly
from .parsers.namespacequantity import NameSpaceQuantity
from .parsers.quantityspacename import QuantitySpaceName

PARSERS = [
    NameOnly,
    NameSpaceQuantity,
    QuantitySpaceName,
]


def parse(string: str) -> tuple[str, int]:
    normalized_string = normalize_string(string)

    if not is_legal_string(normalized_string):
        raise ParserError("Illegal string")

    for parser in PARSERS:
        try:
            name, quantity = parser.parse(normalized_string)
        except (ConverterError, ParserError, ValidatorError):
            continue
        else:
            if not is_valid_name(name):
                raise ParserError("Invalid name")
            if not isinstance(quantity, int):
                raise ParserError("Invalid quantity")
            return name, quantity
    else:
        raise ParserError("All parsers failed")
