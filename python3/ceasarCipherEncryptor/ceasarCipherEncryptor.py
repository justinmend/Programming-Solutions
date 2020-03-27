'''
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".
'''


def caesarCipherEncryptor(string, key):
    # Assumptions:
    # 1. Are we only using english alphabets for our letters? Yes.

    # Note
    # We are given a non-emtpy string.
    # String contains only lowercase letters
    # Input key >= 0

    # Brute Force:
    # We can use an array to map our letters? ASCII?

    # Use python3 ord() to get character's integer unicode value and use chr() vice versa.
    # Alphabet integer values starts at 96 ('a')
    # Use modulo to handle large key size input
    # We check if letterIdx is greater than 122 since 122 is where the alphabet letter stops.
    # If so, we will need to wrap it back to the beginning (96) and we do this by subtracting 26.
    # Return the resultStr list a string by using join method.

    newKey = key % 26
    resultStr = []
    for c in string:
        letterIdx = ord(c) + newKey

        if letterIdx > 122:
            letterIdx = letterIdx - 26

        resultStr.append(chr(letterIdx))

    return "".join(resultStr)

    # Time Complexity - O(N):
    # N represents the length of the string input where we iterate through each character once.

    # String concatenation:
    # Space Complexity - O(N^2):
    # String concatenation takes O(N^2) space since we are making a copy of a new string for
    # every character in the string input.
    # Strings are immutable so everytime we are concatenating a letter to the result string we are
    # actually making another copy of a string with the new letter.
    # Use join method instead since it takes linear space to create a new string out of
    # iterable of string elements.

    # String join():
    # Space Complexity - O(N):
    # N represents the length of the input string. Size of our resultStrArray is proportionate
    # to the length of the input string.
