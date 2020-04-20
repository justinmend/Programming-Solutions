# Time - O(W * H)
# W represents the width of the matrix
# H represents the height of the matrix
# We will iterate through each cell in the matrix only once since we avoid doing repeated work
# by marking visited cells.

# Space - (W * H)
# Worst case is the matrix contains only 1s (river).
# We would then have to recursively call each cell in the matrix which would then
# take up space in our call stack frame.
def riverSizes(matrix):
    # Assumptions:
	
	# Notes:
	# 1. Given a 2d array of potentially unequal height and width containing
	# only 0's and 1's.
	# 0's represent land and 1's represent river
	# 2. A river consist of 1's that are either horizontal or vertically adjacent.
	# Not diagnonally.
	# 3. Return array of the sizes of all rivers in the input matrix in no particular order.
	
	
	# Brute Force:
	# DFS
	
	result = []
	
	# Time - O(2(W * H)) -> O(W * H) | Space - O(W * H)
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			# Inspect cell if it's value is 1 (land)
			if matrix[row][col] == 1:
				# Call getRiversizes to recursively get the size of the river
				# Append returned value of getRiversize to the result array
				result.append(getRiverSize(row, col, matrix))
	return result

# Time - O(W * H)
# We will iterate through each cell in the matrix only once since we avoid doing repeated work
# by marking visited cells.

# Space - O(W * H)
# Worst case is the matrix contains only 1s (river).
# We would then have to recursively call each cell in the matrix which would then
# take up space in our call stack frame.
def getRiverSize(row, col, matrix):
	count = 0
	if matrix[row][col] == 1:
		count += 1
	
	# make sure to mark the cell visited so we don't get stuck in a loop
	matrix[row][col] = -1
	
	# call the getValidMovements method to get all the movements
	movements = getValidMovements(row, col, matrix)
	
	# Recursively call getRiverSizes and pass in all the valid movements
	# Make sure to append the returned values to the count variable
	for move in movements:
		count += getRiverSize(move[0], move[1], matrix)
	
	return count

# Time - O(1) | Space - O(1)
def getValidMovements(row, col, matrix):
	# Get the valid movements to go to from the current cell
	# Check if index is withing range of matrix and cell is a river
	movements = []
	# Up
	if row - 1 >= 0 and matrix[row-1][col] == 1:
		movements.append((row-1, col))
	# Down
	if row + 1 < len(matrix) and matrix[row+1][col] == 1:
		movements.append((row+1, col))
	# Left
	if col - 1 >= 0 and matrix[row][col-1] == 1:
		movements.append((row, col-1))
	# Right
	if col + 1 < len(matrix[0]) and matrix[row][col+1] == 1:
		movements.append((row, col+1))
		
	# return all the movements as tuples in an array
	return movements