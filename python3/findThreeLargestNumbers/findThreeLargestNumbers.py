'''
  Write a function that takes in an array of integers and, without sorting the
  input array, returns a sorted array of the three largest integers in the input
  array.
'''

# Time - O(N) | Space - O(1)
# N represents the length of the input array.


def findThreeLargestNumbers(array):
    # Assumptions:
    # 1. We are given an array with length greater than or equal to 3?
    # 2. Array can contain duplicate numbers.

    # Notes:
    # 1. Given an array of integers
    # 2. Cannot sort the input array
    # 3. Return a sorted array of the three largest integers in the input array.

    # Brute Force:
    # Have three variables to keep track of the three largest numbers?

    # How to do we keep on updating the three variables anytime we see a larger number?
    # Swap values between first, second, and third?

    firstLarge = None
    secondLarge = None
    thirdLarge = None

    for i, num in enumerate(array):
        if thirdLarge is None or num > thirdLarge:
            thirdLarge, secondLarge, firstLarge = num, thirdLarge, secondLarge
        elif secondLarge is None or num > secondLarge:
            secondLarge, firstLarge = num, secondLarge
        elif firstLarge is None or num > firstLarge:
            firstLarge = num

    return [firstLarge, secondLarge, thirdLarge]
