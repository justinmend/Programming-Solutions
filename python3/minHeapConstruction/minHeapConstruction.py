# Assumptions:

# Notes:
# 1. Heap should be represented in the form of an array
# 2. Parent Index formula: (i - 1)//2
# 3. Children Index formula:  Left (2i + 1), Right (2i + 2)

# Brute Force:

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	# Time - O(P * D) | Space - O(1)
	# P represnts the amount of parent indexes in the heap that we need to call siftDown for.
	# The amount of parent indexes in the heap array is half of the heap array length.
	# D represents the max depth of the heap.
	# We call siftDown for every parent index. Sift down takes O(D) time
    def buildHeap(self, array):
        # Get last parent index using parent index formula
		# Work way up to the first parent index
		# Call siftDown on every parent index
		# Iterate in reverse order starting from last parent index
		lastIdx = len(array) - 1
		lastParentIdx = (lastIdx - 1)//2

		# Add 1 to range to handle exclusive rule
		for i in reversed(range(lastParentIdx + 1)):
			self.siftDown(i, array)

		return array

	# Time - O(D) | Space - O(1)
	# D represents the max depth of the heap.
	# Worst case is we have to sift down the biggest value in the heap starting from
	# the root (or first index in array), we would have to sift down the value all the way down the
	# the bottom of the heap. For every level in the heap we traverse through, we encounter one value to compare with whether
	# we need to continue swapping and traversing down.
    def siftDown(self, parentIdx, array):
        # Get child indices using child index formula
		# Compare parent value to both children to decide if sifting down
		# is necessary.
		arrayLen = len(array)
		leftChildIdx = parentIdx * 2 + 1

		while leftChildIdx < arrayLen:
			idxToSwap = leftChildIdx  # Initialize to leftChildIdx by default

			rightChildIdx = (parentIdx * 2 + 2) if (parentIdx *
			                 2 + 2) < arrayLen else -1
			# compare left child and right child values to decide which child index to compare with parent
			if rightChildIdx != -1 and array[leftChildIdx] < array[rightChildIdx]:
				idxToSwap = leftChildIdx
			else:
				idxToSwap = rightChildIdx

			if array[idxToSwap] < array[parentIdx]:
				self.swap(idxToSwap, parentIdx, array)
				parentIdx = idxToSwap
				leftChildIdx = parentIdx * 2 + 1
			else:
				break

	# Time - O(D) | Space - O(1)
	# D represents the max depth of the heap.
	# Worst case is we have to sift up the smallest value in the heap starting from
	# the bottom of the heap (or last index in array), we would have to sift up the value all the way up to the
	# the root of the heap. For every level in the heap we traverse through, we encounter one value to compare with whether
	# we need to continue swapping and traversing up.

    def siftUp(self, curIdx):
        # Get parentIdx using parentIdx formula
		parentIdx = (curIdx - 1)//2

		while parentIdx >= 0:
			if self.heap[curIdx] < self.heap[parentIdx]:
				self.swap(curIdx, parentIdx, self.heap)
				curIdx = parentIdx
				parentIdx = (curIdx - 1)//2
			else:
				break
	# Time - O(1) | Space - O(1)

    def peek(self):
        return self.heap[0]

	# Time - O(D) | Space - O(1)
    def remove(self):
		# Swap first element with last element in array
		# Pop last element to remove
        # Use siftDown method on first element
		self.swap(0, len(self.heap) - 1, self.heap)
		self.heap.pop()
		self.siftDown(0, self.heap)

	# Time - O(D) | Space - O(1)
    def insert(self, value):
        # Add element at last index
		# Call siftUp on last index
		self.heap.append(value)
		lastIdx = len(self.heap) - 1
		self.siftUp(lastIdx)

	# Time - O(1) | Space - O(1)
	def swap(self, i, j, array):
		array[i], array[j] = array[j], array[i]
