import unittest
from solution import brute_force, calculate_prefix, calculate_kadane


class TestMethods(unittest.TestCase):

    def test_bruteforce(self):
        self.assertEqual(brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]), (6, 3, 6))

    def test_prefix(self):
        self.assertEqual(calculate_prefix([-2, 1, -3, 4, -1, 2, 1, -5, 4]), (6, 3, 6))

    def test_kadane(self):
        self.assertEqual(calculate_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]), (6, 3, 6))


if __name__ == '__main__':
    unittest.main()
