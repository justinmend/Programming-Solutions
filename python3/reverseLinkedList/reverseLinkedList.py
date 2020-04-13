'''
  Write a function that takes in the head of a Singly Linked List, reverses the
  list in place (i.e., doesn't create a brand new list), and returns its new head.
'''
# Time - O(N) | Space - O(1)
def reverseLinkedList(head):
	# Notes:
	# 1. Given a head node of a singly linked list.
	# 2. Reverse list in place
	# 3. Return the list with the new head
	
	# Brute Force:
	# Use 3 pointers?
	
    prevNode = None 
	curNode = head
	nextNode = None
	
	while curNode:
		# Get the next node after the current node. We need the reference to the next node
		# after the current node in order to continue traversing the list. 
		
		# Since we will be pointing the current node's next pointer to the
		# previous node, current node will lose reference to the rest of the untraversed list.
		# So, we need to store the next node after the current node temporarily 
		# so that we reference it later and get back to the rest of the untraversed list.
		nextNode = curNode.next
		
		# Point the current node's next pointer to the previous node
		curNode.next = prevNode
		
		# After connecting the current node to the previous node, we can now move up
		# and update the pointer nodes.
		prevNode = curNode
		curNode = nextNode
	
	return prevNode