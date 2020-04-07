'''

  Write a function that takes in a sorted array of integers as well as a target
  integer. The caveat is that the integers in the array have been shifted by
  some amount; in other words, they've been moved to the left or to the right by
  one or more positions. For example, [1,2,3,4] might have turned into [3,4,1,2].

  
  The function should use a variation of the Binary Search algorithm to
  determine if the target integer is contained in the array and should return
  its index if it is, otherwise -1.
'''
# Time - O(log(N)) | Space - O(1):
# N represents the length of the input array.
# Binary Search takes O(log(N))
# We only use auxiliary space.
def shiftedBinarySearch(array, target):
    # Assumptions:
	
	# Notes:
	# 1. Given a sorted array of integers
	# 2. Also, given a target integer
	# 3. Use a variation of the binary search algorithm to solve problem
	# 4. Return the target integer's index if is in the input array else return -1
	
	
	# Brute Force:
	# How do we dictate which direction to go?
	
	leftIdx = 0
	rightIdx = len(array) - 1
	
	# Zero-based index so use less than or equal to for the while loop argument.
	while leftIdx <= rightIdx:
		# Calculate the midIdx
		midIdx = (leftIdx + rightIdx)//2
		
		# Exact match, return index
		if array[midIdx] == target:
			return midIdx
		
		# Check left:
		# Default to check left as long as value at left index is less than or equal to the mid value.
		# We want to check the side where the values in the array are as much sorted as possible.
		elif array[midIdx] >= array[leftIdx]:
			# Still need to check if the left side has the values within range of our target.
			if target < array[midIdx] and target >= array[leftIdx]:
				rightIdx = midIdx - 1
			# Even though we defaulted to check the left side first, our target value is not within that range so we have to go
			# to the right side.
			else:
				leftIdx = midIdx + 1
				
		# Check right:
		else:
			# Still need to check if the right side has the values within range of our target.
			if target > array[midIdx] and target <= array[rightIdx]:
				leftIdx = midIdx + 1
			else:
				rightIdx = midIdx - 1
	
	return -1