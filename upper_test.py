from upper import uppercase
import unittest


class Upper(unittest.TestCase):

    def test_upper(self):
        uppercase_string = uppercase("This is coding at best")
        self.assertEqual(uppercase_string.upper(), "THIS IS CODING AT BEST")
if __name__ == '__main__':
    unittest.main()
