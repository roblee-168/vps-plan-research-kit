# ::ILANG [TYPE:test][BOUNDARY:synthetic arithmetic inputs only]
import unittest
from decimal import Decimal
from cost import calculate
class CostTests(unittest.TestCase):
    def test_renewal(self):
        self.assertEqual(calculate(24,12,4,24),(Decimal(72),Decimal(3)))
    def test_full_commitment(self):
        self.assertEqual(calculate(24,12,4,6),(Decimal(24),Decimal(4)))
    def test_invalid(self):
        for args in [(-1,12,4,24),(24,0,4,24),(24,12,4,0),('NaN',12,4,24)]:
            with self.assertRaises(ValueError): calculate(*args)
