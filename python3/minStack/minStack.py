'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

# Implement using a stack
# Assumptions:
# 1. Do we have to create and design our own node object?


class Node:
    def __init__(self, value):
        # Create a property minValue that keeps track of the current minValue from the range of the current node
        # to it's children nodes?
        self.value = value
        self.minValue = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Create a stack list that will hold our nodes
        # Stack - LIFO
        self.stack = []

    def push(self, x: int) -> None:
        # Create a node
        # Set it's value
        # Set the global min value; take the min between this current node value and the
        # previous min value? Utilize getMin().
        # Push node into stack
        temp = Node(x)
        currMin = self.getMin()
        if currMin == None or x < currMin:
            currMin = x
        temp.minValue = currMin
        self.stack.append(temp)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) <= 0:
            return None
        return self.stack[-1].value

    def getMin(self) -> int:
        # Get the top element and return it's minValue
        # How do we get the top element?
        # Retrieve the top element by calling stack[-1], that is, get the last element in the list?

        # What if the stack is empty? Return none or sys.maxsize?
        if len(self.stack) <= 0:
            # raise ValueError('No min value since stack is empty')
            return None

        return self.stack[-1].minValue

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
