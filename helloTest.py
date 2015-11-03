from hello import hello_world
import unittest


class MyTest(unittest.TestCase):
    def test_hello_world(self):
        greeting = hello_world("Hello World")
        self.assertEqual(greeting, "Hello World")

if __name__ == '__main__':
    unittest.main()
