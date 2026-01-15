import unittest

from palindromes import is_palindrome

class palindrome_test (unittest.TestCase):
    def test_pali_is_true(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("a racecar"))

class palindrome_caps_test (unittest.TestCase):
    def test_pali_has_caps(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("Level"))

if __name__ == "__main__":
    unittest.main()