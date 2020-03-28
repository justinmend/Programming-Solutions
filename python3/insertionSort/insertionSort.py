'''
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort algorithm to sort the array.
'''

def insertionSort(array):
	# Assumptions:
	# 1. Sort in place? Yes. 
	# 2. Are we given a non empty array? No.
	
	# Note:
	
	# Brute Force:
	# Iterate through array (start at index 1):
	# keep track of last index of sorted part of list.
	# Compare current value to the sorted part of list.
	# Use a while loop to iterate through the sorted part of list:
		# Compare current index value to previous index value and see if swapping is necessary.
	
	for i in range(1, len(array)):
		j = i
		while j > 0:
			if array[j] < array[j-1]:
				array[j], array[j-1] = array[j-1], array[j]
			else:
				break
			j -= 1
	
	return array

	# Time Complexity - O(N^2):
	# N represents the length of input array. Worst case is the original input array
	# is already sorted in reverse. We would have to compare every item in the input array
	# to all the other items in the sorted sublist of the array.
	
	# Space Complexity - O(1):
	# We are only using auxiliary space. We are also sorting in place for the input array.