
'''
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first 2 numbers as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..
'''


def getNthFib(n):
    # Assumptions:
    # 1. Are we given a positive integer? n > 0? No, n can be 0.

    # Note:
    # For this case, retrieval of fibonnaci numberis off by 1 in index.
    # EX:
    # 1. getNthFib(1) equals 0 instead of 1
    # 2. getNthFib(3) equals 1 instead of 2

    # Brute Force:
    # Use dp?

    # 1. Create a dp list to cache our previous calculations.
    # 2. Initialize dp[0] and dp[1] to values of 0 and 1 respectively.
    # 3. Check if n < = 1 return 0
    # 4. Iterate through the range of n (start at index 2):
    # Set current dp value to the sum of the previous 2 dp values.
    # 5. Return dp[n-1] as our answer.
    # We use n-1 since in this case, since we are off by 1
    # for the fibonnaci retrieval in this problem example.

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    if n <= 1:
        return 0

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

    # Time Complexity - O(N):
    # N represents the input value n. We iterate through the range of n once.

    # Space Complexity - O(N):
    # N represents the total amount of calculations in our dp list. The size of our dp list is
    # proportionate to the value of input n.
