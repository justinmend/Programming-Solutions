'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        # Implement using Binary Search
        # Assumptions:

        # Note:
        # 1. Input is guaranteed to be a non-negative integer

        # Brute force:
        # 1.Calculate the mid value and repeat to half the search range.
        # 2. Check if the mid value is a square root of x. If so return mid value.
        # Check by making sure x is greater than or equal to the root of the mid value
        # and also check that x is less than the root of the number to the right of the mid value.
        # We do these checks so that we know whether we still need to check the left side or right side of the mid value to find
        # the correct mid value who's root is equal to x.
        # 3. Adjust the left and right range accordingly depending if we need to check the left side or right side from the mid value.

        l, r = 0, x
        mid = None

        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1

        return mid

        # Time Complexity - O(log(n)):
        # Binary Search algorithm takes log(n)

        # Space Complexity - O(1):
        # We are only using auxiliary space.
