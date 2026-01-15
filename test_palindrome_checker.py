import unittest

class smoke_test (unittest.TestCase):
    def test1plus1(self):
        self.assertEqual(1+1, 2)

if __name__ == "__main__":
    unittest.main()