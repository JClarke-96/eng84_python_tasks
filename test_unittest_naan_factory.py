# Import code that will test
from naan_factory import NaanFactory
import unittest


class NaanTest(unittest.TestCase):
    NaanFact = NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.NaanFact.make_dough("water", "flour"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.NaanFact.bake_dough("dough"), "naan")

    def test_run_factory(self):
        self.assertEqual(self.NaanFact.run_factory("water", "flour"), "naan")
