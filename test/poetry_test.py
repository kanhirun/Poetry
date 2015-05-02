import pytest
import unittest

from poetry import Poetry
from generators import alphabetGenerator


class PoetryTest(unittest.TestCase):

  def testAreRhymingWords(self):
    poetry = Poetry()
    w1 = "pills"
    w2 = "ills"

    results = poetry.areRhymingWords(w1, w2)

    self.assertEqual(True, results)


  def testLastWord(self):
    poetry   = Poetry()
    line     = "I hope this problem"
    expected = "problem"

    results = poetry._lastWord(line)

    self.assertEqual(expected, results)


  def testOnlyWordLastWord(self):
    poetry   = Poetry()
    line     = "problem"
    expected = "problem"

    results = poetry._lastWord(line)

    self.assertEqual(expected, results)


  def testBoughtEndingPattern(self):
    """
    The ending pattern of `bought` is `ought`.
    """
    poetry        = Poetry()
    word          = "bought"
    endingPattern = "ought"

    results = poetry.endingPattern(word)

    self.assertEqual(endingPattern, results)


  def testSpyingEndingPattern(self):
    """
    The ending pattern of `spying` is `ying`, because `y` acts as a vowel.
    """
    poetry        = Poetry()
    word          = "spying"
    endingPattern = "ying"

    results = poetry.endingPattern(word)

    self.assertEqual(endingPattern, results)


  def testAllEndingPattern(self):
    """
    The ending pattern of `all` is itself.
    """
    poetry        = Poetry()
    word          = "all"
    endingPattern = "all"

    results = poetry.endingPattern(word)

    self.assertEqual(endingPattern, results)


  def testAppleIsALegalWord(self):
    """
    `apple` is a word because...
    (1) every letter belongs in a-zA-Z,
    (2) there is at least one vowel—in this example, there are exactly 2.
    """
    poetry = Poetry()
    word   = "apple"

    results = poetry.isLegalWord(word)

    self.assertEqual(True, results)


  def testRpmmvIsNotALegalWord(self):
    """
    `Rpmmv` is not a legal word, because there are no vowels.
    """
    poetry = Poetry()
    word = "Rpmmv"

    results = poetry.isLegalWord(word)

    self.assertEqual(False, results)


  def testRymmvIsALegalWord(self):
    """
    In the word, `Rymmv`, y acts as a vowel, therefore `Rymmv` is a legal word.
    """
    poetry = Poetry()
    word = "Rymmv"

    results = poetry.isLegalWord(word)

    self.assertEqual(True, results)


  def test4ppleIsNotALegalWord(self):
    """
    A legal word does not contain numbers, because it does not belong in
    a-zA-Z.
    """
    poetry = Poetry()
    word = "4pple"

    results = poetry.isLegalWord(word)

    self.assertEqual(False, results)


  def testCharacterIsLetter(self):
    poetry    = Poetry()
    character = "a"

    results = poetry.isLetter(character)

    self.assertEqual(True, results)


  def testCharacterIsNotLetter(self):
    """
    The test example tests a (possible) edge case on using ASCII calculations
    to determine whether a character is a letter.
    """
    poetry    = Poetry()
    character = "["

    results = poetry.isLetter(character)

    self.assertEqual(False, results)


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

    results = poetry.isVowel(letter, 1, 3)  # y is the 2nd letter of a
                                            # 3-letter word, therefore it is a
                                            # vowel

    self.assertEqual(True, results)


  def testYIsNotAVowel(self):
    poetry = Poetry()
    letter = "y"

    results = poetry.isVowel(letter, 0, 3)  # y is the first letter, therefore
                                            # it is not a vowel

    self.assertEqual(False, results)


  def testYLastIsNotAVowel(self):
    poetry = Poetry()
    letter = "y"

    results = poetry.isVowel(letter, 3, 3)  # y is the last letter, therefore
                                            # it is not a vowel

    self.assertEqual(False, results)
