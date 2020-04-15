'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Implement using backtracking

        # Assumptions:

        # Notes:
        # 1. Given integer n pairs of parentheses. n >= 0
        # 2. Return all combinations of well-formed parentheses in a string list

        # Brute Force:
        # When appending to a string, open parentheses >= close parentheses

        result = []

        # Create a recursive helper method.
        # Call recursion function
        # Pass in number of open paren and closed paren, empty string, result array
        self.generateParenthesisHelper(0, 0, "", result, n)

        return result

    # Time - O(2^N):
    # N represents the integer n input value.
    # The 2 represents the branching factor for the two recursion calls inside our recursive method.
    # How many time the recursion method keeps branching out depends on when the strings we are building
    # fulfill the n pairs of parentheses requirements, that is, it's string length is (2 * N).
    # Therefore, our time complexity is O(2^2N) and if we remove the constant it is O(2^N)

    # Space - O(N):
    # We make N recursion calls which takes up space in the stack frame.
    # We only make N exact recursion calls to create our string.
    # We avoid making branch 2^N recursion calls since we have checks
    # to make sure we make only N amount of recursion calls, that is, we have exact n pairs of parentheses.
    def generateParenthesisHelper(self, openCount, closeCount, string, result, n):
        # Base case:
        if openCount == n and closeCount == n:  # 0 == 3 and 0 == 3
            # Append string to result array
            result.append(string)
            return

        if openCount <= n:
            self.generateParenthesisHelper(
                openCount + 1, closeCount, string + "(", result, n)
        if closeCount < openCount:
            self.generateParenthesisHelper(
                openCount, closeCount + 1, string + ")", result, n)
