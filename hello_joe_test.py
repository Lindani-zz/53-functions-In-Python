from hello_joe import hello_joe
import unittest


class MyTest(unittest.TestCase):
    def test_hello_world(self):
        lowercase_j = hello_joe("joe")
        self.assertEqual(lowercase_j, "Hello")

        uppercase_j = hello_joe("Joe")
        self.assertEqual(uppercase_j, "Hello")

        b_lowercase = hello_joe("bob")
        self.assertEqual(b_lowercase, "Hello")

        b_uppercase = hello_joe("Bob")
        self.assertEqual(b_uppercase, "Hello")

        unknown_username = hello_joe("Lindani")
        self.assertEqual(unknown_username, "Lindani")
if __name__ == '__main__':
    unittest.main()
