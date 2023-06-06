from unittest import TestCase

from eveparser.errors import ParserError
from eveparser.parsers.quantityspacename import QuantitySpaceName


class NameOnlyTestCase(TestCase):
    def test_example_passes(self):
        self.assertEqual(QuantitySpaceName.parse("2 Ragnarok"), ("Ragnarok", 2))

    def test_no_space_fails(self):
        self.assertRaises(ParserError, QuantitySpaceName.parse, "Ragnarok")

    def test_string_quantity_fails(self):
        self.assertRaises(ParserError, QuantitySpaceName.parse, "string Ragnarok")
