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

	# parent formula: (i-1)//2
	# child formula: Left: (2i + 1)//2, Right: (2i + 2)//2

	# Time - O(N) | Space - O(1)
    def buildHeap(self, array):
        lastIdx = len(array)-1
		lastParentIdx = (lastIdx-1)//2

		for i in reversed(range(lastParentIdx + 1)):
			self.siftDown(i, array)

		return array

	# Time - O(log(N)) | Space - O(1)
    def siftDown(self, parentIdx, array):
        # Compare parent to children and swap as needed
		leftChildIdx = (2 * parentIdx + 1)

		idxToSwap = leftChildIdx

		while leftChildIdx < len(array):
			rightChildIdx = (2 * parentIdx + 2) if (2 *
			                 parentIdx + 2) < len(array) else -1

			if rightChildIdx != -1 and array[leftChildIdx] > array[rightChildIdx]:
				idxToSwap = rightChildIdx

			if array[idxToSwap] < array[parentIdx]:
				self.swap(idxToSwap, parentIdx, array)
				parentIdx = idxToSwap
				leftChildIdx = (2 * parentIdx + 1)
				idxToSwap = leftChildIdx
			else:
				break

	# Time - O(log(N)) | Space - O(1)

    def siftUp(self, curIdx, array):
        parentIdx = (curIdx - 1)//2

		while curIdx > 0:
			if array[curIdx] < array[parentIdx]:
				self.swap(curIdx, parentIdx, array)
				curIdx = parentIdx
				parentIdx = (curIdx - 1)//2
			else:
				break

	# Time - O(1) | Space - O(1)
    def peek(self):
        return self.heap[0]

	# Time - O(log(N)) | Space - O(1)
    def remove(self):
        # swap first elem and last elem
		# pop last elem
		# bubble down from first index (0)
		# return array

		self.swap(0, len(self.heap)-1, self.heap)
		itemToRemove = self.heap.pop()
		self.siftDown(0, self.heap)
		return itemToRemove

	# Time - O(log(N)) | Space - O(1)
    def insert(self, value):
        # Insert at end of array
		# sift up
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)

	# Time - O(1) | Space - O(1)
	def swap(self, i, j, array):
		array[i], array[j] = array[j], array[i]
