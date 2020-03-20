'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Implement using a map
        # Assumptions:
        # 1. Input string contains only lowercase alphabets

        # Brute force:
        # 1. Check if the length of both input strings are the same.
        # 2. Map the letter and frequency for string s
        # 3. Iterate through string t:
        # Check if the letter exist in the map
        # If it exists decrement frequency value
        # Else return false
        # 4. Iterate through values of the map:
        # If we encountera value that is not zero return False
        # 5. Return true if we succesfully iterate through the values

        if len(s) != len(t):
            return False

        my_map = {}

        for c in s:
            my_map[c] = my_map.get(c, 0) + 1

        for c in t:
            if c in my_map:
                my_map[c] -= 1
            else:
                return False

        for value in my_map.values():
            if value != 0:
                return False

        return True

        # Time Complexity - O(N) - N = S + T + A, S represents string s length, T represents string t length.
        # A represents the number of different alpahbet letters that can be added to the map but this can be ignored assuming
        # we are only given alphabet letters as there are only 26 alphabet letters.
        # Space Complexity - O(1) - Assuming that there are only 26 alphabet letters, the map size would then be constant.
