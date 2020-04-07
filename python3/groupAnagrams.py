# Time - O(W * Nlog(N) + M) -----> O(W * Nlog(N))
# W represents the total amount words in the words list. We iterate through the words list once.
# N represents the length of the longest string in the words list.
# It takes O(Nlog(N)) time to sort a word in alphabetical order.
# M represents the total amount of values (grouped anagrams) in our map/dictionary.
# M gets outbounded by the bigger time complexity of O(W * Nlog(N)) so we can ignore M.

# Space - O(2(W * N)) --------> O(W * N)
# W represents the total amount words in the words list.
# N represents the length of the longest string in the words list.
# We create a map and also return the result list of anagrams strings as our answer. 
# Both are (W * N) size so it is O(2(W * N)) but we can remove the constant therefore it is O(W * N)
# For each string word W, it's string space size is N.
def groupAnagrams(words):
    # Assumptions:
	
	# Notes:
	# 1. Given an array of strings
	# 2. Anagrams are strings made up of exactly the same letters where order doesn't matter.
	# 3. Return a list of anagram groups in no particular order
	
	
	# Brute Force:
	# Map the frequency of the characters of the string?
	# Compare each string to other strings?
	
	# Sort the string and then compare? We would still need the original order of that string.
	# How do we keep track of which group to add in the list?
	# Create a dictionary where the sorted string is the key?
	
	# Sort string and store in temp variable, check if temp string is in the map.
	# If it is in the map, add the original string to the value list of that key
	# Else, create a new key and list value with the original string
	
	result = []
	my_map = {}
	
	for word in words:
		sortedString = ''.join(sorted(word))
		if sortedString in my_map:
			my_map[sortedString].append(word)
		else:
			my_map[sortedString] = [word]
	
	for value in my_map.values():
		if len(value) != 0:
			result.append(value)
	
	return result