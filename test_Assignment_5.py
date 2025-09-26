import unittest
from Assignment_5 import fahrenheit_to_celsius, fibonacci

class TestTemperatureConversion(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("32")

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_numbers(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(TypeError):
            fibonacci("5")

if __name__ == '__main__':
    unittest.main()