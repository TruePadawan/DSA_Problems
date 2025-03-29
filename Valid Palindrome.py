'''
loop through the string and create a new string with only alphanumeric chars
check that its the same when it is reversed
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        return new_str == new_str[::-1]