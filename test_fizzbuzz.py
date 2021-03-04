import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fizzBuzz(5), ['1','2','Fizz','4','Buzz'])
    
if __name__ == '__main__':
    unittest.main(verbosity=2)