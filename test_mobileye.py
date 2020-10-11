import unittest

from mobileye import split_string


class TestMobileye(unittest.TestCase):
    def test_short_words_short_string(self):
        self.assertEqual(["hi hi hi"], split_string("hi hi hi"))

    def test_short_words_long_string(self):
        self.assertEqual(["hi hi hi", "hi hi hi", "hi hi hi", "hi"], split_string("hi hi hi hi hi hi hi hi hi hi"))

    def test_string_with_ten_character_word(self):
        self.assertEqual(["what a", "disgusting", "food"], split_string("what a disgusting food"))

    def test_string_starting_with_ten_character_word(self):
        self.assertEqual(["disgusting", "what a", "food"], split_string("disgusting what a food"))

    def test_string_with_longer_than_ten_character_word(self):
        self.assertEqual(["Avadakedav", "ra", "alohomora"], split_string("Avadakedavra alohomora"))
