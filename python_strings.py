import random
import string


class StringsFunctions:
    # - Check if a string is a palindrome or not

    @staticmethod
    def check_if_string_is_palindrome(given_string):
        palindrome = ""

        for i in reversed(given_string):
            palindrome += i

        if given_string == palindrome:
            return True
        else:
            return False

    # - Find the longest word in a sentence

    @staticmethod
    def get_longest_word_from_sentence(sentence):
        longest_word = ""

        words = sentence.split()

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

        return longest_word

    # - Check if two strings are anagrams of each other

    @staticmethod
    def check_if_2_strings_are_anagrams(first_word, second_word):
        is_anagram = True

        for letter in first_word:
            if letter in second_word:
                second_word = second_word.replace(letter, '', 1)
            else:
                is_anagram = False

        if second_word != "":
            is_anagram = False

        if is_anagram:
            return True
        else:
            return False

    # - Reverse a string

    @staticmethod
    def reverse_string(given_string):
        return given_string[::-1]

    # - Find the most common word in a phrase

    @staticmethod
    def most_common_word_in_a_phrase(sentence):
        most_common_word = {
            "word": "",
            "occurrence": 0
        }

        words = sentence.split()
        print(words)

        for word in words:
            occurrence = words.count(word)
            if occurrence > most_common_word["occurrence"]:
                most_common_word["occurrence"] = occurrence
                most_common_word["word"] = word

        return most_common_word['occurrence']

    # - Generate a random password

    @staticmethod
    def generate_a_password(password_length):
        password = ""

        for i in range(password_length):
            password += random.choice(string.printable)

        return password

    # - Find the most frequent letter in a string

    @staticmethod
    def get_most_common_letter_in_a_string(given_string):
        most_common_letter = {
            "letter": "",
            "occurrence": 0
        }

        for letter in given_string:
            occurrence = given_string.count(letter)
            if occurrence > most_common_letter["occurrence"]:
                most_common_letter["occurrence"] = occurrence
                most_common_letter["letter"] = letter

        return most_common_letter['letter']
