'''

  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.
  
  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.
'''

# Time - O(N) | Space - O(1)
# N represents the length of the input array.
def moveElementToEndSolution1(array, toMove):
    # Assumptions:
	# 1. What is the maximum size possible we can recieve for the input array?
	# The time efficiency of our sorting algorithm is dependent on the size of our input array.
	
	# Notes:
	# 1. Given an array of integers
	# 2. Also, given an integer
	# 3. Move all instances of that integer in the array to the end of the array. In-place sorting?
	# 4. Return the array as the answer
	# 5. Other integers can be ordered differently
	
	# Brute Force:
	i = 0
	j = len(array) - 1
	
	while i < j:
		leftNum = array[i]
		rightNum = array[j]
		
		if leftNum != toMove:
			i += 1
		
		if rightNum == toMove:
			j -= 1
			
		swap(i, j, array)
			
	return array

# Time - O(N^2) | Space - O(1)
# N represents the length of the input array.
# Modified bubble sort takes O(N^2) time.
def moveElementToEndSolution2(array, toMove):
    # Assumptions:
	# 1. What is the maximum size possible we can recieve for the input array?
	# The time efficiency of our sorting algorithm is dependent on the size of our input array.
	# 
	
	# Notes:
	# 1. Given an array of integers
	# 2. Also, given an integer
	# 3. Move all instances of that integer in the array to the end of the array. In-place sorting?
	# 4. Return the array as the answer
	# 5. Other integers can be ordered differently
	
	# Brute Force:
	# Modified bubble sort?
	# Instead of comparing values by greater than or less than, compare if the current value matches the toMove value?
	
	isAllEleMoved = False

	while not isAllEleMoved:
		isAllEleMoved = True
		
		for i in range(len(array) - 1):
			# if current value is equal toMove and 
			# current value is not the same as the value,
			# swap to the right
			num = array[i]
			nextNum = array[i + 1]
			if num == toMove and num != nextNum:
				swap(i, i+1, array)
				isAllEleMoved = False
	
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]