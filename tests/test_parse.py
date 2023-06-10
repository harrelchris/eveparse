from unittest import TestCase

from eveparse import parse
from eveparse.errors import ParserError


class ParseTestCase(TestCase):
    def test_all_examples_pass(self):
        self.assertEqual(parse("Capital Transverse Bulkhead I	1	Rig Armor	Module	Rig Slot"), (33902, "Capital Transverse Bulkhead I", 1))
        self.assertEqual(parse("Cybernetic Subprocessor - Basic	1	Cyber Learning	Implant	"), (9943, "Cybernetic Subprocessor - Basic", 1))
        self.assertEqual(parse("Ragnarok 2"), (23773, "Ragnarok", 2))
        self.assertEqual(parse("Ragnarok* 2"), (23773, "Ragnarok", 2))
        self.assertEqual(parse("Ragnarok x2"), (23773, "Ragnarok", 2))
        self.assertEqual(parse("2 Ragnarok"), (23773, "Ragnarok", 2))
        self.assertEqual(parse("Ragnarok"), (23773, "Ragnarok", 1))
        self.assertEqual(parse("4 x Ragnarok"), (23773, "Ragnarok", 4))
        self.assertEqual(parse("3x Ragnarok"), (23773, "Ragnarok", 3))

    def test_invalid_name_fails(self):
        self.assertRaises(ParserError, parse, "string")
