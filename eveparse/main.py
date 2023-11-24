from eveparse import exceptions
from eveparse.parsers import assets
from eveparse.parsers import compare
from eveparse.parsers import contract
from eveparse.parsers import inventory

parsers = [
    assets.view_contents_container,
    assets.view_contents_ship,
    compare.dynamic_columns,
    contract.multiple_items,
    contract.multiple_items_no_details,
    inventory.details,
    inventory.icons,
]


def parse(text: str) -> dict:
    items = {}
    errors = []
    for line in text.splitlines():
        normalized_line = line.casefold()
        if not line.strip():
            continue
        for parser in parsers:
            try:
                type_dict = parser(normalized_line)
            except exceptions.ParserException:
                continue
            else:
                for type_id, quantity in type_dict.items():
                    if type_id in items:
                        items[type_id] += quantity
                    else:
                        items[type_id] = quantity
                break
        else:
            errors.append(line)
    return dict(items=items, errors=errors)