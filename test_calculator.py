import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(substract(1, 1), 0)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(divide(12, 4), 3)

if __name__ == '__main__':
    unittest.main()
