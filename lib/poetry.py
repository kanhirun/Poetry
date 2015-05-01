class Poetry(object):

  def __init__(self):
    self.VOWELS = set(["a", "e", "i", "o", "u"])
    super()


  def isLetter(self, character):
    val = ord(character)

    return (65 <= val <= 90) or (97 <= val <= 122)  # a-zA-Z


  def isVowel(self, letter, letterIndex, maxIndex):
    return (letter in self.VOWELS) or \
           (letter is "y" and (letterIndex != 1 and letterIndex != maxIndex))
