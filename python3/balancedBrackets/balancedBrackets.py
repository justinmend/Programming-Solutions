# Time - O(N) | Space - (M)
# N represents the length of the input string where we iterate through it once.
# M represents the size of our stack.
# Worst case is the string contains all open brackets
# which would require us to push all closed brackets into the stack.


def balancedBrackets(string):
    # Assumptions:
    # 1. Given only valid bracket characters?

    # Notes:

    # Brute Force:
    # Use a stack?
    # Create a map for the brackets?
    # Iterate through each character in the string.
    # For every open bracket we encounter, we
    # push into the stack the same type of closed bracket for the open bracket.

    # If we encounter a closed bracket, we pop an item from the stack
    # and compare to the closed bracket.
    # If they are not the same, return False
    # return True if stack is empty

    d = {'{': '}', '(': ')', '[': ']'}

    stack = []

    for c in string:
        if c in d:
            stack.append(d[c])
        else:
            if len(stack) == 0:
                return False
            else:
                popBracket = stack.pop()
                if popBracket != c:
                    return False

    return len(stack) == 0
