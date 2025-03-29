class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highest_substr_length = 0
        substr = ""
        substr_length = 0
        for char in s:
            if char in substr:
                substr_length = len(substr)
                if substr_length > highest_substr_length:
                    highest_substr_length = substr_length

                substr = substr + char
                split_index = substr.index(char)
                substr = substr[split_index + 1 :]
            else:
                substr = substr + char
                substr_length = len(substr)

        # The whole string is the largest substring
        if highest_substr_length == 0:
            return len(s)
        # In case the last substr is the largest substring
        if substr_length > highest_substr_length:
            highest_substr_length = substr_length
        return highest_substr_length


test = Solution()
print(test.lengthOfLongestSubstring("dvdf"))
