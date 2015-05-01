class Poetry(object):
  def __init__(self):
    self.VOWELS = set(["a", "e", "i", "o", "u"])
    super()

  def isVowel(self, letter, letterIndex, maxIndex):
    return (letter in self.VOWELS) or \
           (letter is "y" and (letterIndex != 1 and letterIndex != maxIndex))
