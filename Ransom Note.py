'''
Form a count of the characters in magazine
    loop through the chars in magazine
        get the count and last index of the char
        update the iterator to start from the last index
for each char in ransomNote
    if it's not in char_count keys or the count is 0:
        return False
return True
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Build a hash map containing each letter in magazine and how many times they appear
        char_count = {}
        for char in magazine:
            if char_count.get(char) is None:
                char_count[char] = 1
            else:
                char_count[char] += 1
        
        for char in ransomNote:
            if char_count.get(char) is None or char_count.get(char) == 0:
                return False
            elif char_count.get(char) is not None and char_count.get(char) > 0:
                char_count[char] -= 1
        return True