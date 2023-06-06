from unittest import TestCase

from eveparser.errors import ParserError
from eveparser.parsers.namespacequantity import NameSpaceQuantity


class NameOnlyTestCase(TestCase):
    def test_example_passes(self):
        self.assertEqual(NameSpaceQuantity.parse("Ragnarok 2"), ("Ragnarok", 2))

    def test_no_space_fails(self):
        self.assertRaises(ParserError, NameSpaceQuantity.parse, "Ragnarok")

    def test_string_quantity_fails(self):
        self.assertRaises(ParserError, NameSpaceQuantity.parse, "Ragnarok string")
