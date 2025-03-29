'''
Given n as the initial argument, Recursively fun the function for n-1 until n == 1
If n == 1, return "1"
initialize a string 'result' = what the previous rec
For each char in the returned string
    use regex to find the number of consecutive occurrences of each char in the string
concat the count and the string, add it to result
return result
'''

import re


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = self.countAndSay(n-1)
        encoded_str = ""
        size = len(result)
        while size != 0:            
            current_char = result[0]
            count = len(re.search(rf"{current_char}+", result).group())
            encoded_str += str(count)+current_char
            result = result[count:]
            size = len(result)
        return encoded_str

test = Solution()
print(test.countAndSay(4))