import unittest
from python_strings import StringsFunctions


class TestStringsFunctions(StringsFunctions, unittest.TestCase):

    def test_check_if_string_is_palindrome_function(self):
        assert self.check_if_string_is_palindrome("abcba")
        assert not self.check_if_string_is_palindrome("abcde")

    def test_get_longest_word_from_sentence_function(self):
        assert self.get_longest_word_from_sentence("My cat is a good cat") == "good"
        assert self.get_longest_word_from_sentence("cat") == "cat"

    def test_check_if_2_strings_are_anagrams_function(self):
        assert self.check_if_2_strings_are_anagrams("mariaDB", "maDBrai")
        assert not self.check_if_2_strings_are_anagrams("mariaDB", "mariaSM")

    def test_reverse_string_function(self):
        assert self.reverse_string("something") == "gnihtemos"
        assert self.reverse_string("123") == "321"

    def test_most_common_word_in_a_phrase_function(self):
        assert self.most_common_word_in_a_phrase("something about something of smth") == "something"
        assert self.most_common_word_in_a_phrase("something about about something about") == "about"

    def test_generate_a_password_function(self):
        assert len(self.generate_a_password(3)) == 3
        assert self.generate_a_password(0) == ""

    def test_get_most_common_letter_in_a_string_function(self):
        assert self.get_most_common_letter_in_a_string("Everyday I spent my time, coding fine") == "e"
        assert self.get_most_common_letter_in_a_string("aa bb eee sss dd") == "e"
        assert self.get_most_common_letter_in_a_string("") == ""


if __name__ == '__main__':
    unittest.main()
