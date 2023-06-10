import functools

from .constants import TYPES
from .converters import normalize_string
from .errors import ConverterError, ParserError, ValidatorError
from .validators import is_int, is_legal_string, is_valid_name

from .parsers.contract import Contract
from .parsers.contractnodetails import ContractNoDetails
from .parsers.nameonly import NameOnly
from .parsers.namespacequantity import NameSpaceQuantity
from .parsers.namespacexquantity import NameSpaceXQuantity
from .parsers.quantityspacename import QuantitySpaceName
from .parsers.quantityspacexspacename import QuantitySpaceXSpaceName
from .parsers.quantityxspacename import QuantityXSpaceName

PARSERS = [
    NameOnly,
    Contract,
    ContractNoDetails,
    NameSpaceQuantity,
    NameSpaceXQuantity,
    QuantitySpaceName,
    QuantitySpaceXSpaceName,
    QuantityXSpaceName,
]


@functools.cache
def parse(string: str) -> tuple[int, str, int]:
    normalized_string = normalize_string(string)

    if not is_legal_string(normalized_string):
        raise ParserError("Illegal string")

    for parser in PARSERS:
        try:
            parsed_name, parsed_quantity = parser.parse(normalized_string)
        except (ConverterError, ParserError, ValidatorError):
            continue
        else:
            if not is_valid_name(parsed_name):
                if not parsed_name.endswith("*"):
                    continue
                else:
                    parsed_name = parsed_name.strip("*")
                    if not is_valid_name(parsed_name):
                        continue
            inv_type = TYPES[parsed_name]
            type_id = inv_type["type_id"]
            name = inv_type["name"]
            return type_id, name, parsed_quantity
    else:
        raise ParserError("All parsers failed")
