import unittest
from io import StringIO
from unittest.mock import patch
from main import add_numbers, fizzbuzz, fibonacci, find_max, find_min


class TestMockPython(unittest.TestCase):

    # Test Exercise 1
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-2, 8), 6)
        self.assertEqual(add_numbers(0, 0), 0)

    # Test Exercise 2
    @patch("sys.stdout", new_callable=StringIO)
    def test_fizzbuzz_output(self, mock_stdout):
        fizzbuzz(15)
        output = mock_stdout.getvalue().strip().split("\n")
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        self.assertEqual(output, expected)

    # Test Exercise 3
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(10), 55)

    # Test Exercise 4
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-10, -5, -1]), -1)
        self.assertEqual(find_max([7]), 7)
        self.assertIsNone(find_max([]))

    # Test Exercise 5
    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-10, -5, -1]), -10)
        self.assertEqual(find_min([7]), 7)
        self.assertIsNone(find_min([]))


if __name__ == "__main__":
    unittest.main()
