from upper import uppercase
import unittest


class UpperTest(unittest.TestCase):

    def test_upper(self):
        uppercase_string = uppercase("This is coding at best")
        self.assertEqual(uppercase_string, "THIS IS CODING AT BEST")
if __name__ == '__main__':
    unittest.main()
