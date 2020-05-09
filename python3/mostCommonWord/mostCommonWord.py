# Time - O(C * P + B) | Space - O(C * P + B)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Assumptions:

        # Notes:
        # 1. Given a string representing a paragraph.
        # 2. Given a list of strings consisting of banned words.
        # 3. Return the most frequent word that is not in the list of banned words.
        # Return the answer in lowercase.
        # 4. It is guarantedd there is at least one word that isn't banned.

        # Brute Force:
        # Convert string into lowercase
        # Remove the following characters [!?',;.]
        # Split string into a list of words

        # Map the frequency of the words in the paragraph.
        # Needs to be sorted from greatest to least frequency.
        # Use ordered list?
        # Map the list of banned words for constant lookup.

        # Iterate through keys and return the
        # First occurence in the map of a word where it is not banned.

        # Time - O(B) | Space - O(B)
        banset = set(banned)

        # Time - O(C * P) | Space - O(C * P)
        # C represents the total amount of symbols to be removed from paragraph
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        # Time - O(P) | Space - O(P)
        # P represents the length of the paragraph string
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0

        # Time - O(P) | Space - O(1)
        # Bounded by the length of the count dictionary.
        # Worst case is all the words except for the last word in count are in the banset.
        # We would have to iterate through all the word items in count.
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans
