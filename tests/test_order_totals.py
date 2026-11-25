import unittest

from src.order_totals import subtotal_yen


class TestDemoTotals(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(subtotal_yen([]), 0)

    def test_multiple_lines(self):
        self.assertEqual(subtotal_yen([(1200, 2), (450, 3)]), 3750)

    def test_zero_quantity(self):
        self.assertEqual(subtotal_yen([(1500, 0)]), 0)

    def test_very_large_positive_integer_price_and_quantity(self):
        result = subtotal_yen([(10**30 + 1, 10**30 - 1)])
        self.assertEqual(result, 10**60 - 1)
        self.assertIs(type(result), int)

    def test_negative_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            subtotal_yen([(100, -1)])

    def test_boolean_is_not_an_integer(self):
        with self.assertRaises(TypeError):
            subtotal_yen([(True, 1)])


if __name__ == '__main__':
    unittest.main()
