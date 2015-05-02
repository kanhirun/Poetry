class Poetry(object):

  VOWELS = set(["a", "e", "i", "o", "u"])  # excludes the conditional vowel, y.

  def endingPattern(self, word):
    n = len(word)
    i = (n - 1)
    j = -1

    while (i >= 0):
      currLetter = word[i]
      if self.isVowel(currLetter, i, n):
        j = (i - 1)
        break
      i -= 1

    while (j >= 0):
      currLetter = word[j]
      if (not self.isVowel(currLetter, j, n)):
        return word[j+1:n]
      j -= 1

    return word


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

    return (areLetters and hasVowel)


  def isLetter(self, char):
    val = ord(char)

    return (65 <= val <= 90) or (97 <= val <= 122)


  def isVowel(self, letter, letterIndex, maxIndex):
    return (letter in self.VOWELS) or \
           (letter is "y" and (letterIndex != 0 and letterIndex != maxIndex))
