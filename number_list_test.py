from number_list import numberList
import unittest


class MyTest(unittest.TestCase):
    def test_hello_world(self):
        myList = numberList(10)
        self.assertEqual(myList, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()
