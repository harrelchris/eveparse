from unittest import TestCase

from eveparser import parse
from eveparser.errors import ParserError


class ParseTestCase(TestCase):
    def test_all_examples_pass(self):
        self.assertEqual(parse("Ragnarok 2"), ("Ragnarok", 2))
        self.assertEqual(parse("2 Ragnarok"), ("Ragnarok", 2))
        self.assertEqual(parse("Ragnarok"), ("Ragnarok", 1))

    def test_invalid_name_fails(self):
        self.assertRaises(ParserError, parse, "string")
