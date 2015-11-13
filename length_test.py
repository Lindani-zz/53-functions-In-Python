from length import paremeter_length
import unittest


class Paremeter_length(unittest.TestCase):

    def test_paremeter_length(self):
        results = paremeter_length("this is good practice")
        self.assertEqual(len(results), 21)

if __name__ == '__main__':
    unittest.main()
