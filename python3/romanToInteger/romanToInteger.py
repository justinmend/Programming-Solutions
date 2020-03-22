'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        # Implement using a map
        # Assumptions:
        # 1. Given a valid input of roman numeral

        # Note:
        # Input is guaranteed to be within the range of 1 to 3999

        # Brute Force:
        # 0. Check if length of s is 1, if so return the roman numeral value in integer of that character in s.
        # 1. Map the roman symbols to their respective values.
        # 2. Initialize our result variable with the roman numeral value in integer of the first character in string s.
        # 3. Iterate through each character in the string (start at index 1):
        # 4. If the current character's roman numeral value is greater than the previous roman numeral value, subtract the
        # current roman numeral value to the previous roman numeral value (multiply by 2). The reason we multiply by 2 of the previous
        # roman numeral value so that we don't add that value twice to our result. Add the calculation result to our result variable.
        # Else, add the current roman numeral value to our result as normal.
        # 5. Return our result value as the answer

        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if len(s) == 1:
            return d[s[0]]

        result = d[s[0]]

        for i in range(1, len(s)):
            if d[s[i]] > d[s[i-1]]:
                result += d[s[i]] - (d[s[i-1]] * 2)
            else:
                result += d[s[i]]

        return result

        # Time Complexity - O(S):
        # S represents the length of the input string s. We iterate through each character in strin s once.

        # Space Complexity - O(1):
        # We are only using auxiliary space so space complexity is constant.
