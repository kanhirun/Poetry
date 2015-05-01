class Poetry(object):

  VOWELS = set(["a", "e", "i", "o", "u"])

  def isLegalWord(self, word):
    areLetters = True
    hasVowel   = False
    n          = len(word)

    for (i, char) in enumerate(word):
      if (not self.isLetter(char)):
        areLetters = False
        break
      if (not hasVowel) and self.isVowel(char, i, n):
        hasVowel = True 

    return areLetters and hasVowel


  def isLetter(self, char):
    val = ord(char)

    return (65 <= val <= 90) or (97 <= val <= 122)


  def isVowel(self, letter, letterIndex, maxIndex):
    return (letter in self.VOWELS) or \
           (letter is "y" and (letterIndex != 1 and letterIndex != maxIndex))
