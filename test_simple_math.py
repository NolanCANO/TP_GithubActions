import unittest
from simple_math import simple_math

class test_simple_math(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simple_math.addition(2, 3), 5)

    
    def test_soustraction(self):
        self.assertEqual(simple_math.soustraction(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
