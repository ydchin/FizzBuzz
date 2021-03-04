import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz, 'Hello World!')
    

if __name__ == '__main__':
    unittest.main()