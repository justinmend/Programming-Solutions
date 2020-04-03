'''
  Write a function that, given a string, returns its longest palindromic
  substring.

  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.

  You can assume that there will only be one longest palindromic substring.
'''
# Time - O(N^2):
# N represents the length of the input string.
# For each character in the string, we potentially iterate through the string again up to the range of the
# length of the input string. This is when we are expanding the substring search trying to find the longest palindromic substring.

# Space - O(1): Only using auxiliary space


def longestPalindromicSubstring(string):
    # Assumptions:

    # Notes:
    # 1. Single character strings are palindromes
    # 2. There will only be one longest palindromic substring.
    # 3. A palindrome is a string that's written the same forward and backward.

    # Brute Force:
    # Expand from the center and check the left and right outermost if they are equal?
    # What if the substring is odd or even length, how do we check for palindromicity?
    # How much does it cost to create substrings? Are we adding extra space?

    # We iterate through each character in the string.
    # We then expand and check for palindromicity.
    # Create a helper method to get the indices of the lps
    # Use a while loop and two pointers; j and k
    # Make sure j and k are within boundaries.
    # j goes to left (j--), k goes to right (k++)

    # Odd:
    # Compare previous character and next character if they are the same.

    # Even:
    # Compare current character to the previous character if they are the same.

    lpsIndices = [0, 0]

    for i in range(len(string)):
        odd = getLongestPalindromeIndices(i-1, i+1, string)
        even = getLongestPalindromeIndices(i-1, i, string)
        # Update lpsIndices by comparing currnet lpsIndices to odd and even
        # Take max, use lambda to deteriine key for comparing max
        lpsIndices = max(lpsIndices, odd, even, key=lambda x: x[1] - x[0])

    return string[lpsIndices[0]:lpsIndices[1] + 1]  # +1 to handle inclusive


def getLongestPalindromeIndices(left, right, string):

    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    # Redact increment and decrement in indices from the function call to return the last valid
    # lps indices.
    return [left + 1, right - 1]
