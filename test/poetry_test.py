import pytest
from unittest import TestCase

from poetry import Poetry


class PoetryTest(TestCase):
  def testLetterIsAVowel(self):
    poetry = Poetry()
    letter = "a"

    results = poetry.isVowel(letter, 2, 3)  # factory boy?

    self.assertEqual(True, results)  # AssertionError


  def testLetterIsNotAVowel(self):
    poetry = Poetry()
    letter = "r"

    results = poetry.isVowel(letter, 2, 3)  # factory boy?

    self.assertEqual(False, results)


  def testYIsAVowel(self):
    poetry = Poetry()
    letter = "y"

    results = poetry.isVowel(letter, 2, 3)  # y is the 2nd letter of a
                                            # 3-letter word, therefore it is a
                                            # vowel

    self.assertEqual(True, results)


  def testYIsNotAVowel(self):
    poetry = Poetry()
    letter = "y"

    results = poetry.isVowel(letter, 1, 3)  # y is the first letter, therefore
                                            # it is not a vowel

    self.assertEqual(False, results)


  def testYLastIsNotAVowel(self):
    poetry = Poetry()
    letter = "y"

    results = poetry.isVowel(letter, 3, 3)  # y is the last letter, therefore
                                            # it is not a vowel

    self.assertEqual(False, results)
