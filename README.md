# Eve Parser

Parser for Eve Online - extract item name and quantity from a string

## Install

```shell
pip install eveparser
```

## Usage

```python
import eveparser

string = "Ragnarok 1"

name, quantity = eveparser.parse(string)
```

## Failure

The parser will return raise an error if it is unable to parse the string.

## Development

## Setup

```shell
scripts\build
```

## Update SDE

```shell
python scripts\sde.py
```

### Test

```shell
python -m unittest
```
