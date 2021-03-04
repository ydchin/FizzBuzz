import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fizzBuzz(5), ['1','2','Fizz','4','Buzz'])
    def test3(self):
        self.assertEqual(fizzbuzz.fizzBuzz(15), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
    
if __name__ == '__main__':
    unittest.main(verbosity=2)