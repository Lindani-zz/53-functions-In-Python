from reverse import reversed_words
import unittest


class ReversedWords(unittest.TestCase):

    def test_reverse_words(self):
        words = reversed_words("codex is cool")
        self.assertEqual(words, "looc si xedoc")

if __name__ == '__main__':
    unittest.main()
