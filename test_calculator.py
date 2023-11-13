import unittest
from calculator import add, substract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_substract(self):
        self.assertEqual(substract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
