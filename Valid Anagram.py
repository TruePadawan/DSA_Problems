'''
First check that they're of the same length
Create a hash table which keeps track of the char count
Loop through string_a and string_b simultaneously
For each char in string_a:
    add 1 to its count in the table
For each char in string_b:
    subtract 1 from its count in the table
Confirm that all values in the table are 0
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        same_length = len(s) == len(t)
        if not same_length:
            return False
        
        char_count = {}
        for i in range(len(s)):
            char_a = s[i]
            char_b = t[i]
            
            if char_count.get(char_a) is None:
                char_count[char_a] = 1
            else:
                char_count[char_a] += 1
            
            if char_count.get(char_b) is None:
                char_count[char_b] = -1
            else:
                char_count[char_b] -= 1
        values = list(char_count.values())
        for value in values:
            if value != 0:
                return False
        return True