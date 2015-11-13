from reverse import reversed_words
import unittest


class ReversedWords(unittest.TestCase):

    def reverse_words(self):
        words = reversed_words("codex is cool")
        self.assertEqaul(words, "hdjdhdjdldkdh")

if __name__ == '__main__':
    unittest.main()
