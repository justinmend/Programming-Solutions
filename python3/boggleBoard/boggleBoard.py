'''
  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing letters; this matrix represents a boggle board. You're
  also given a list of words.

  
  Write a function that returns an array of all the words contained in the
  boggle board.

  
  A word is constructed in the boggle board by connecting adjacent
  (horizontally, vertically, or diagonally) letters, without using any single
  letter at a given position more than once; while a word can of course have
  repeated letters, those repeated letters must come from different positions in
  the boggle board in order for the word to be contained in the board. Note that
  two or more words are allowed to overlap and use the same letters in the
  boggle board.
'''


def boggleBoard(board, words):
    # Assumptions:
	# Notes:
	# 1. Given a 2d array where width and height may not be the same.
	# 2. 2d array contains letters.
	# 3. Also, given a list of words
	# 4. Return an array of all the words contained in the 2d array
	# 5. Words can be connected through adjacent neighbors (horizontal, vertical, and diagonal)
	
	# Brute Force:
	# Use a trie?
	
	# Iterate through each word in the words list.
		# Create helper method for creating trie
		
		# Check if the word already exist in the trie to avoid having to search the 2d array.
		# If it exists in the trie then it also exists in the 2d array.
			# Automatically add word to the result list.
		
		# Else, it means it does not exist in the trie so we have to explore the 2d array to see if it exists there instead.
			# Create helper method for checking if the word is in the matrix.
			# Explore every cell in the matrix.
			# Only check the cell if the character in the cell matches the curent character of the word.
			# If the character does match skip and go to the next cell.
				# Create a explore helper method to use for recursion
			
			# After exploring in the 2d array and we find it exists in there, 
			# we generate the trie for each sublists of the current word.
			# Add the current word to the result list
			
	# return result
	
	result = []
	trie = Trie()
	
	for word in words:
		if trie.containsWord(word):
			result.append(word)
		else:
			if boardContainsWord(word, board):
				trie.create(word)
				result.append(word)
	
	return result

# Time - O(R * C * 8^S)| Space - O(8^S):
# R represents the height of the board.
# C represents the width of the board.
# S represents the length of the word.
# The explore function method takes O(8^S) both in time and space.
def boardContainsWord(word, board):
	for row in range(len(board)):
		for col in range(len(board[row])):
			if explore(word, 0, row, col, board):
				return True
	
	return False

# Time - O(8^S): 
# S represents the length of the word.
# 8 directions to possibly branch off in recursion calls at the same time : top-left, top-right, bottom-left, bottom-right, up, down, left, right
# Each recursion call will continue to recursively make the 8 branched off calls, up to the length of the word.

# Space - O(8^S):
# S represents the length of the word.
# We make O(8^S) recursion calls which takes up space in our call stack frame.
def explore(word, chIdx, row, col, board):
	# Make sure to explore all neighbors including diagonally.
	# Make sure to mark visited cells.
	
	# BASE CASE:
	if chIdx == (len(word) - 1) and word[chIdx] == board[row][col]:
		return True
	
	if word[chIdx] == board[row][col]:
		# Mark visited
		board[row][col] = -1
		movements = getValidNeighbors(row, col, board)
		
		# 8 possible directions to branch off in recursion: top-left, top-right, bottom-left, bottom-right, up, down, left, right
		for move in movements:
			# Every branched off recursion call will continue to branch off recursion calls with the 8 different directions.
			# We have the base case to handle terminating the recursion call when we've successfuly found the all the characters we need for the word
			# in the matrix. We increment chIdx by 1 in our recursion call as we look for the next character we need for the word in the matrix.
			if explore(word, chIdx + 1, move[0], move[1], board):
				# Need to undo marking of visit before returning true immediately
				board[row][col] = word[chIdx]
				return True
			
		# Undo marking of visit
		board[row][col] = word[chIdx]

	return False

# Time - O(1) | Space - O(1)
def getValidNeighbors(i, j, board):
	neighbors = []
	if i > 0 and j > 0 and board[i-1][j-1] != -1: # upper left
		neighbors.append([i - 1, j - 1])
	if i > 0 and j < len(board[0]) - 1 and board[i-1][j+1] != -1: # upper right
		neighbors.append([i-1, j+1])
	if i < len(board) - 1 and j < len(board[0]) - 1 and board[i+1][j+1] != -1: # bottom right
		neighbors.append([i+1, j+1])
	if i < len(board) - 1 and j > 0 and board[i+1][j-1] != -1: # bottom left
		neighbors.append([i + 1, j-1])
	if i > 0 and board[i-1][j] != -1: # Up
		neighbors.append([i-1, j])
	if i < len(board) - 1 and board[i+1][j] != -1: # Down
		neighbors.append([i+1, j])
	if j > 0 and board[i][j-1] != -1: # Left
		neighbors.append([i, j-1])
	if j < len(board[0]) - 1 and board[i][j+1] != -1: # Right
		neighbors.append([i, j+1])
	
	return neighbors

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
	
	# Time - O(N) | Space - O(N)
	def create(self, word):
		curNode = self.root
		
		for c in word:
			if c in curNode:
				curNode = curNode[c]
			else:
				curNode[c] = {}
				curNode = curNode[c]
				
		curNode[self.endSymbol] = True
	
	# Time - O(N) | Space - O(1)
	def containsWord(self, word):
		curNode = self.root
		
		for c in word:
			if c in curNode:
				curNode = curNode[c]
			else:
				return False
		
		return self.endSymbol in curNode
		
	
	
		
