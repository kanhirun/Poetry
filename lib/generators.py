def alphabetGenerator():
  """
  Yields a sequence of alphabets starting from a-z, then A-Z.
  """
  current    = 96
  breakpoint = 122
  newCurrent = 64
  limit      = 90

  while (current != limit):
    if (current == breakpoint):
      current = newCurrent
    else:
      current += 1
      yield chr(current)
