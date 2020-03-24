'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        # Assumptions:
        # 1. Given an input string with length > 0?
        # 2. Given a valid input string, that is, valid characters?
        # 3. Is non sequential lates of 3 accounts not rewarded? Or only sequential lates considered non-rewarded? EX: Reward for LPLL and no reward for PLLL?
        # Only sequential lates are not rewarded.
        
        # Note:
        # Reward if A < 2 or L < 3
        
        # Brute Force:
        # Only reset value for key "L" if we encounter new character.   
        # Map the record character and the frequency
        # Check as we map, if the key's values haven't reached the limit, that is, A < 2 or L < 3. If attendance record reach max for "A" and "L" return False immediately
        # Return true at the end after mapping the keys succesfully
    
        if len(s) == 0:
            return True
        
        record_map = {}
        record_map[s[0]] = 1
        
        for i in range(1, len(s)):
            # Check if the key's values haven't already reach the limit, return False immediately if 'A' >= 2 or 'L' >= 3
            # Compare current character and previous character if they are the same. If previous character is "L", reset it's value
            
            c = s[i]
            
            record_map[c] = record_map.get(c, 0) + 1
            
            if c == 'A':
                if record_map[c] >= 2:
                    return False
            if c == 'L':
                if record_map[c] >= 3:
                    return False
            
            if c != s[i-1]:
                if s[i-1] == 'L':
                    record_map[s[i-1]] = 0
                    
            
        
        return True
        
        # Time Complexity - O(N) - N for iterating through string s
        # Space Complexity - O(M) - M for map size
        