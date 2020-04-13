'''
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Quick Sort algorithm to sort the array.
'''
# Time - O(N^2):
# N represents the length of the input array
# We are essentialy iterating through all the possible sublist of input array therefore
# time complexity is O(N^2).

# Space - O(log(N)):
# N represents the length of the input array
# Quick sort makes O(log(N)) recurison calls and this takes up space in the stack frame.
def quickSort(array):
	# Assumptions:
	
	# Notes:
	# 1. Given an array of integers
	# 2. Return a sorted version of that array.
	# 3. Use quick sort algorithm to sort array.
	
	# Brute Force:
	# Use recursion
	
    quickSortHelper(array, 0, len(array)-1)
	return array
  
def quickSortHelper(arr,low,high): 
	if low < high: 
		# Separately sort elements.
		# Elements less than pivot are on the very left of the 
		# sublist and elements greater than pivot are on very right of sublist.
		# pI (partition index) is the wall that divides the elements less than the pivot and elements
		# greater than the pivot.
		pi = partition(arr,low,high) 
		
		quickSortHelper(arr, low, pi-1) 
		quickSortHelper(arr, pi+1, high) 

def partition(arr,low,high): 
    # Partition index that divides the sublist between the elements smaller than pivot
	# and elements bigger than pivot.
	pIdx = low         
    pivot = arr[high]
	
	for i in range(low , high): 
		# If current element is smaller than the pivot, we swap.
		if arr[i] < pivot: 
			swap(pIdx, i, arr)
			# increment partition index
			pIdx += 1
	
	# Swap the values between pivot index and partition index incremented.
	# We want to put the pivot value in between the now partitioned values of the sublist.
	# Values less than the pivot are on the left side of the sublist and values
	# greater than the pivot are on the right side of the sublist.
	swap(pIdx, high, arr)
    
	return pIdx

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]