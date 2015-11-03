from hello_uppercase import hello_uppercase
import unittest


class MyTest(unittest.TestCase):
    def test_hello_world(self):
        uppercase = hello_uppercase("lindani")
        self.assertEqual(uppercase, "LINDANI")

if __name__ == '__main__':
    unittest.main()
