from sum_list import sum_list
import unittest


class MyTest(unittest.TestCase):
    def test_sum_list_for_3(self):
        sumList = sum_list(3)
        self.assertEqual(sumList, 6)

    def test_sum_list_for_7(self):
        sumList = sum_list(7)
        self.assertEqual(sumList, 28)

    def test_sum_list_for_20(self):
        sumList = sum_list(20)
        self.assertEqual(sumList, 210)

    def test_sum_list_for_0(self):
        sumList = sum_list(0)
        self.assertEqual(sumList, 0)


if __name__ == '__main__':
    unittest.main()
