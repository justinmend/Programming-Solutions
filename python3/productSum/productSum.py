'''
Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it should be summed themselves and then multiplied by their level of depth. For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

'''


def productSum(array):
    # Assumptions:
    # 1. Input array is non-empty

    # Note:

    # Brute Force:
    # Use recursion?
    # How do we keep track of current depth?
    # How should we call the recursion method and traverse correctly through the multi-level array?

    # Create a product sum variable
    # Call the recursive function and set to product sum value
    # Initialize level value to 1 when calling recursive function
    productSum = productSumRecursive(1, array)

    return productSum


def productSumRecursive(level, array):
    # Create a helper method as a recursive function:
    # Perameters are:
    # 1. current level
    # 2. Array to pass into
    # Base case?

    # Create a temp sum variable
    tempSum = 0

    # Iterate through the array list:
    # Check if the current value is a list. Use type() method to check if the item is a list.
    # Call the recursive function and set to add temp sum.
    # Increment level by 1 when calling recursive function.
    # Else add to the temp sum.
    for item in array:
        if type(item) is list:
            tempSum += productSumRecursive(level + 1, item)
        else:
            tempSum += item

    # What does the recursive function return?
    # Return the temp sum of the values in the array multiplied by the current level.
    return level * tempSum

    # Time Complexity - O(N):
    # N represents the total amout of items we iterate through in the input array. We iterate through the array once
    # using recursion.

    # Space Complexity - O(N):
    # N represents the greatest depth level that we will encounter in the array. For every level we go into deeper, we incur
    # into the recursion stack frame which takes up space.
