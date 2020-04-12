'''

  Write a function that takes in the head of a Singly Linked List that contains
  a loop (in other words, the list's tail node points to some node in the list
  instead of None/null). 
  
  The function should return the node (the actual node--not just its value) from which the loop originates
  in constant space.
'''

# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Assumptions:

# Notes:
# 1. Given a head node of a singly linked list that contains a loop.
# 2. Return the node from which the loop originates.

# Brute Force:

# Time - O(N) | Space - O(1)


def findLoop(head):
    # D represents the distance from the head all the way to the node of where the loop originates.
    # P represents the distance from where the loop originates all the way to where both the slow and
    # fast pointer met.

    # Total distance where both pointers meet.
    # Let Slow ptr = x
    # Let Fast ptr = 2x, since it travels twice faster

    # Let x = D + P
    # Fast ptr = 2(D+P) = 2D + 2P

    # Let T represent the total distance or length of the list excluding the extra loops, that is,
    # the distance starting from the head all the way to the tail right before it loops again.

    # So, T = 2D + 2P - P

    # We subtract P to eliminate the extra distance the fast pointer made from extra loops
    # in the cycle.

    # Therefor it is, T = 2D + P

    # Let R represent the distance we want to find starting
    # from where the two pointers met all the way to where the loop originates.

    # R = T - D - P

    # We subtract D and P since we only want the distance starting from where the
    # two pointers met and all the way to the origin of the loop.

    # Plugin the T equation:
    # R = 2D + P - D - P

    # The distance D, which is starting from the head of the node all the way to where the
    # two pointers meet is also the same as distance R, which is starting from where the two pointers
    # met and then all the way to where the loop originates.

    # Therefore:
    # R = D

    slow = head.next
    fast = head.next.next

    # Fast pointer moves twice as fast.
    # Increment both pointers until they meet each other.
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    # Reset one of the pointers back to the head of the list
    slow = head
    # Increment both the pointers at the same speed until they both meet.
    # They will both land at the spot where the loop in the list originates.
    # Remember R = D, both have the same amount of distance to travel to get to the origin of the loop.
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Return either one of the pointers since they will both return
    # where the loop originates.
    return slow
