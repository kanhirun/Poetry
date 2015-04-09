# Poetry

## Problem Statement

Given a poem, determine its rhyme scheme.

To simplify things, because English is such a fickle language, there are some constraints:

A legal word is a sequence of lower or uppercase letters, containing at least one vowel, where a vowel is ‘a’, ‘e’, ‘i’, ‘o’, or ‘u’. Also, ‘y’ is considered a vowel if it is not at the start or end of a word. Words are delimited by spaces.

Two words are considered rhyming if they have the same ending pattern (defined below). This comparison is case-insensitive (see Example 1.)

An ending pattern is a substring of a word such that:

1. The word ends with that substring,
2. The substring contains exactly one contiguous string of vowels,
3. The first letter of the substring is a vowel, and
4. The substring must either be the whole string, or the letter immediately preceding the start of the substring must be a non vowel.

For example, the ending pattern of “bought” is “ought”, the ending pattern of “spying” would be “ying”, and the ending pattern of “all” would be “all”. (Note that “spy” has no vowels, and thus is not a legal word.)

Two lines rhyme if their corresponding last words rhyme, and a line is empty if it contains no words.

The procedure for determinining rhyme scheme is as follows: The first non-empty line in the poem should be labeled with the lowercase letter ‘a’. Every line that rhymes with that line should also be labeled with that letter. The next unlabeled non-empty line should be labeled with the letter ‘b’, and any rhyming lines should also be labeled in this manner. When you run out of lowercase letters, continue by using the uppercase letters ‘A’ to ‘Z’. Empty lines should be labeled with ‘ ‘ (the space character).

The 0th character of the returned String should be the rhyme scheme label of the 0th line, the 1st character should be the label of the 1st line, and so on. This means that the returned String will have the same number of characters as there are elements in poem. Thus, given a String[] poem, then your method should return a String detailing the rhyme scheme.