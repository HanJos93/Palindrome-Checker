import unittest

from palindromes import is_palindrome

class palindrome_test (unittest.TestCase):
    def test_pali_is_true(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("a racecar"))

if __name__ == "__main__":
    unittest.main()