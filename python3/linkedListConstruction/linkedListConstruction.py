# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Assumptions:

# Notes:
# 1. Doubley linked list: Has prev and next pointers

# Brute Force:


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
	
	# Time - O(1) | Space - O(1)
    def setHead(self, node):
		# We need to be able to take existing nodes in the list and set them to become the new head.
		# What if we are inserting a new node as head?
		
        if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.insertBefore(self.head, node)
	
	# Time - O(1) | Space - O(1)		
    def setTail(self, node):
		# We need to be able to take existing nodes in the list and set them to become the new tail.
		if self.tail is None:
			self.setHead(node)
		else:
			self.insertAfter(self.tail, node)
	
	# Time - O(1) | Space - O(1)
    def insertBefore(self, node, nodeToInsert):
        # What if node is head? If node is head that means the node doesn't have a previous element?
		
		# Remove bindings of nodeToInsert
		self.removeBindings(nodeToInsert)
		if node == self.head:
			self.head.prev = nodeToInsert
			nodeToInsert.next = self.head
			self.head = nodeToInsert
		else:
			tempPrev = node.prev
			tempPrev.next, nodeToInsert.prev = nodeToInsert, tempPrev
			nodeToInsert.next, node.prev = node, nodeToInsert
	
	# Time - O(1) | Space - O(1)
    def insertAfter(self, node, nodeToInsert):
        # What if node is tail? If node is tail that means the node doesn't have a next element?
	
		# Remove bindings of nodeToInsert
		self.removeBindings(nodeToInsert)
		
		if node == self.tail:
			self.tail.next = nodeToInsert
			nodeToInsert.prev = self.tail
			self.tail = nodeToInsert
		else:
			tempNext = node.next
			node.next, nodeToInsert.prev = nodeToInsert, node
			nodeToInsert.next, tempNext.prev = tempNext, nodeToInsert
	
	# Time - O(N) | Space - O(1)
	# N represents the total nodes in the linked list.
	# Worst case is the position is the same as the length of the linked list which would require us to traverse through all the nodes in the list.
    def insertAtPosition(self, position, nodeToInsert):
		# Can be a new node or existing node
        # Position is not zero-based index
		
		curNode = self.head
		count = 0
		while count < position and curNode: 
			count += 1
			if count == position:
				self.insertBefore(curNode, nodeToInsert)
				return
			curNode = curNode.next
		
		# Handle edge case where position doesn't exist, do we just add to the end of the list?
		if curNode is None:
			self.setTail(nodeToInsert)
	
	# Time - O(N) | Space - O(1)
	# N represents the total nodes in the linked list.
	# Worst case is the node to be removed is at the end of the linked list which would require us to traverse through all the nodes in the list.
    def removeNodesWithValue(self, value):
        curNode = self.head
		while curNode:
			if curNode.value == value:
				nodeToRemove = curNode
				curNode = curNode.next
				self.removeBindings(nodeToRemove)
			else:
				curNode = curNode.next
	
	# Time - O(1) | Space - O(1)
    def remove(self, node):
		# This block of commented code is already handled in removeBindings() method:
		# if node == self.head:
		# 	self.head = self.head.next
		# if node == self.tail:
		# 	self.tail = self.tail.prev
        self.removeBindings(node)
	
	# Time - O(N) | Space - O(1)
	# N represents the total nodes in the linked list.
	# Worst case is the node with the target value is at the end of the linked list which would require us to traverse through all the nodes in the list.
    def containsNodeWithValue(self, value):
        curNode = self.head
		
		while curNode:
			if curNode.value == value:
				return True
			curNode = curNode.next
			
		return False
	
	# Time - O(1) | Space - O(1)
	def removeBindings(self, node):
		# What if the node is head or tail?
		
		tempPrev, tempNext = node.prev, node.next
		if tempPrev is not None:
			tempPrev.next = tempNext
		if tempNext is not None:
			tempNext.prev = tempPrev
		
		if node == self.head:
			self.head = tempNext
		
		if node == self.tail:
			self.tail = tempPrev
		
		node.prev = None
		node.next = None
