# teststock.py

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    
    def test_create_2(self):
        s = Stock(name = 'GOOG', shares = 100, price = 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

        self.assertEqual(s.cost, 49010)

        s.sell(50)
        self.assertEqual(s.shares, 50)

        stock_from_row = Stock.from_row(["GOOG",50,490.1])
        self.assertIsInstance(stock_from_row, Stock)

        self.assertEqual(s.__repr__(), f"Stock('{s.name}', {s.shares}, {s.price})")

        self.assertEqual(True, stock_from_row.__eq__(s))

    def test_exceptions(self):

        s = Stock('APPL', 100, 250.9)
        with self.assertRaises(TypeError):
             s.shares = '50'
        with self.assertRaises(ValueError):
             s.shares = -50
        with self.assertRaises(TypeError):
             s.price = '50'
        with self.assertRaises(ValueError):
             s.price = -50.1
        with self.assertRaises(AttributeError):
             s.share = -50.1

if __name__ == '__main__':
    unittest.main()