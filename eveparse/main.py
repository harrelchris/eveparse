import exceptions

parsers = [

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
