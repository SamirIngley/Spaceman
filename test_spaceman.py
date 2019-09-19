
import unittest
from spaceman import is_word_guessed
from spaceman import new_get_guessed_word
from spaceman import is_guess_in_word

class TestSpaceman(unittest.TestCase):

    def test_is_word_guessed(self):
        assert is_word_guessed ('yoma', 'yom') == False


    def test_get_guessed_word(self):
        assert new_get_guessed_word('yoma', 'yoma') == True


    def test_is_guess_in_word(self):
        assert is_guess_in_word('m', 'modelicious') == True 


if __name__ == "__main__":
    unittest.main()