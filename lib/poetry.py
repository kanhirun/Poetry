import string


class Poetry(object):

  VOWELS = set(["a", "e", "i", "o", "u"])  # excludes the conditional vowel, y.

  def rhymeScheme(self, poem):
    results       = ""
    knownPatterns = {}  # closed set
    emptySymbol   = " "

    alphabets     = list(string.ascii_letters)
    i = 0
    n = len(alphabets)

    for line in poem:
      lastWord = self._lastWord(line)

      if (not lastWord):
        results += emptySymbol
        continue

      endingPattern = self.endingPattern(lastWord)

      try:
        symbol  = knownPatterns[endingPattern]
      except KeyError:
        symbol = alphabets[i]
        knownPatterns[endingPattern] = symbol
        i += 1

      results += symbol

    return results


  def areRhymingWords(self, w1, w2):
    return (self.endingPattern(w1) == self.endingPattern(w2))


  def endingPattern(self, word):
    _word = word.lower()  # ending patterns are case-insentive
    n = len(_word)
    i = (n - 1)
    j = -1

    while (i >= 0):
      currLetter = _word[i]
      if self.isVowel(currLetter, i, n):
        j = (i - 1)
        break
      i -= 1

    while (j >= 0):
      currLetter = _word[j]
      if (not self.isVowel(currLetter, j, n)):
        substring = _word[j+1:n]
        return substring 
      j -= 1

    return _word


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


  def _lastWord(self, line):
    _line = line.split()

    if _line:
      lastWord = _line[-1]
      return lastWord 
    else:
      return ""
