'''

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

  
  Assume that there will be at most one pair of numbers summing up to the target
  sum.
'''


def twoNumberSumSolution1(array, targetSum):
    # Assumptions:
    # 1. At most one pair of numbers in array summing up to target.

    # Notes:
    # 1. Input is a non-empty array.
    # 2. Return the the numbers that sum up to the target.
    # 3. If no pair sum up to the target return an empty array.

    # Brute Force:
    # Use substraction, then append number to result array.
    # If targetSum != 0, return empty array

    for i in range(len(array)):
        tempResult = [array[i]]
        complement = targetSum - array[i]
        for j in range(i+1, len(array)):
            if array[j] == complement:
                tempResult.append(array[j])
                return tempResult

    return []

    # Time - O(N^2) | Space - O(1)
    # Can we do better in terms of time?


def twoNumberSumSolution2(array, targetSum):

    # Notes:
    # 1. Non empty array of distinct integers.

    # Brute Force:
    # As we iterate through array:
    # Calculate the complement
    # Check if the complement exists in the map, if so
    # return in an array the current number and the complement number
    # Else, map the number as a key and it's value to boolean true

    # If no two sum return an empty array

    d = {}

    for num in array:
        complement = targetSum - num
        if complement in d:
            return [complement, num]
        else:
            d[num] = True

    return []

    # Time - O(N) | Space - O(D)
    # N represents length of array.
    # D represents length of dictionary which is proportionate to the size of the array.
