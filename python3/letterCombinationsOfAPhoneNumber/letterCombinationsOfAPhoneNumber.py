# Time - O(3^N * 4^M) | Space - O(3^N * 4^M)
# N represents the total digits in the input digits string mapped to three letters.
# M represents the total digits in the input digits string mapped to four letters.
# We call the backtrack recursion method (3^N * 4^M) times which accrues in the call stack frame therefore
# space complexity is O(3^N * 4^M).


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Given a string containing digits (2-9)
        # Return all possible letter combinations that the digits string represent

        # Map the digits to their respective list of letters
        mapDigits = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []

        # Backtrack - recursion:
        # For each letter in the list of letters mapped to the first character in digit string,
        # Call backtrack recursion on substring (digit string with first character removed)
        # if length of substring == 0, append current combination string to result list

        if digits:
            self.backtrack("", digits, result, mapDigits)

        return result

    # Time - O(3^N * 4^M) | Space - O(3^N * 4^M)
    def backtrack(self, combination, digits, result, mapDigits):
        if len(digits) == 0:
            result.append(combination)
            return

        for letter in mapDigits[digits[0]]:
            self.backtrack(combination+letter, digits[1:], result, mapDigits)
