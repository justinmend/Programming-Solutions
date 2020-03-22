'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Implement using Binary Search
        # Assumptions:
        # 1. We are given a positive integer num for our input. num > 0

        # Note:
        # Cannot use python built-in library functions such  as sqrt

        # Brute Force:
        # 1. Set start and end values to 1 and num respectively.
        # 2. while start is less than or equal to end:
        # Divide the search in half by calculating the mid value.
        # 3. Check if the current mid value's square is within the target value:
        # If mid * mid <= num < (mid + 1) * (mid + 1), set sqrt_val to mid value and break out of while loop
        # 4. Check if we need to search in the left:
        # Else if num < mid * mid, set end index to mid value - 1
        # 5. Check if wee need to search in the right:
        # Else: set start index to mid value + 1
        # 6. Return true if the square of the sqrt_val equals the target num else return false

        sqrt_val = 0
        start = 1
        end = num

        while start <= end:
            mid = start + (end - start)//2

            if (mid * mid) <= num < (mid + 1) * (mid + 1):
                sqrt_val = mid
                break

            elif num < (mid * mid):
                end = mid - 1
            else:
                start = mid + 1

        return (sqrt_val ** 2) == num

        # Time Complexity - O(log(n)):
        # Binary Search algorithm takes log(n) - the range of our search continually gets divided into half.

        # Space Complexity - (1):
        # We are only using auxiliary space so space complexity is constant.
