from unittest import TestCase

from eveparser.errors import ParserError
from eveparser.parsers.base import TabbedParser, UnTabbedParser


class TabbedParserTestCase(TestCase):
    def test_tabbed_passes(self):
        self.assertEqual(TabbedParser.parse("Ragnarok	1"), None)

    def test_untabbed_fails(self):
        self.assertRaises(ParserError, TabbedParser.parse, "Ragnarok")


class UnTabbedParserTestCase(TestCase):
    def test_untabbed_passes(self):
        self.assertEqual(UnTabbedParser.parse("Ragnarok"), None)

    def test_tabbed_fails(self):
        self.assertRaises(ParserError, UnTabbedParser.parse, "Ragnarok	1")
