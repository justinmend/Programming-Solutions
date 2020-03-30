'''
    Write a MinMaxStack class for a Min Max Stack. The class should support:
    1. Pushing and popping values on and off the stack.
    2. Peeking at the value at the top of the stack.
    3. Getting both the minimum and the maximum values in the stack at any given point in time.

    All class methods, when considered independently, should run in constant time and with constant space.
'''

# Assumptions:

# Notes:
# 1. All class methods,should run in constant time with constant space.
# 2. Do we have to create our own constructor?
# 3. Can I create another class for node class?

# Brute Force:
# How do we keep track of global min and max?
# Create a node class with property value, min, and max?

# Use two stacks? One stack?

# getMin, getMax:
# Should be able to look at top of stack and see the current min and max.

class Node:
	def __init__(self, value, minVal, maxVal):
		self.val = value
		self.min = minVal
		self.max = maxVal

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	# Give property of stack
	# Create init constructor
	def __init__(self):
		self.stack = []
	
	# O(1) - time | O(1) - space	
    def peek(self):
		# What if stack is empty?
		if len(self.stack) == 0:
			return None
		return self.stack[len(self.stack)-1].val
	
	# O(1) - time | O(1) - space	
    def pop(self):
		popVal = self.peek()
		self.stack.pop()
        return popVal

	# O(1) - time | O(1) - space	
    def push(self, number):
		# What if there is no current min or max? That is, stack is empty?
		
    	# Get current min and current max, set to temp variables
		curMin, curMax = self.getMin(), self.getMax()
		# if current min or max is None, automatically set min and max to number value
		if curMin is None or curMax is None:
			curMin, curMax = number, number
		else:
			curMin = min(curMin, number)
			curMax = max(curMax, number)
		
		# Create new node:
		# Give node min value between current min and current value
		# Give node max value between current max and current value
		# Give node current value
		item = Node(number, curMin, curMax)
		# Push node into stack using append
		self.stack.append(item)
	
	# O(1) - time | O(1) - space	
    def getMin(self):
		# What if the stack is empty? Return None?
		if len(self.stack) == 0:
			return None
		
		return self.stack[len(self.stack)-1].min
		
	# O(1) - time | O(1) - space	
    def getMax(self):
		# What if the stack is empty? Return None?
		if len(self.stack) == 0:
			return None
		
		return self.stack[len(self.stack)-1].max