# Assumptions:
# Notes:
# Brute Force:

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

        # Time - O(N^2):
        # N represents the length of the input string.
        # We iterate through every substring of the string.

        # Space - O(N^2):
        #
    def populateSuffixTrieFrom(self, string):
        # Every string added to the trie should end with the special endSymbol character "*"

        # Iterate through each substring of the string:
        # Create a helper method for this?
        # For each character in the substring, check if it already exists in the trie,
        # if so, continue with that character in the trie.
        # Else, create a new key with an empty map, set the current object to map this new object to it.
        # After iterating the substring, set the last nested object to have its value as the end object with the endSymbol signifying the string is complete.

        for i in range(len(string)):
            curTrie = self.root
            for j in range(i, len(string)):
                ch = string[j]
                if ch not in curTrie:
                    curTrie[ch] = {}
                curTrie = curTrie[ch]

            curTrie[self.endSymbol] = True

        # Time - O(N) | Space - O(1)
    def contains(self, string):
        curTrie = self.root
        for i in range(len(string)):
            ch = string[i]
            if ch in curTrie:
                curTrie = curTrie[ch]
            else:
                return False

        return self.endSymbol in curTrie
