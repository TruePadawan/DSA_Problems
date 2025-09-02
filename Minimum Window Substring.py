"""
Initial approach (not optimal enough for all test cases, passes 265 out of 268)

Iterate through s
start the window when a char in t is encountered
    account for it
    if another char in t is encountered > start of window:
        account for it
        set it as the next start if next start is not set
    if all chars in t are accounted for:
        store the substr if its smaller than what is currently stored
        start from the next start (guaranteed to be set)

Better approach from Neetcode: https://www.youtube.com/watch?v=jSto0O4AJbM
"""
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        min_substr_ptr = (-1, -1)
        min_substr_len = math.inf
        # Create a hash map for the char count (t), we use this for constant time operations
        needed_chars, window = {}, {}
        for char in t:
            if needed_chars.get(char) is None:
                needed_chars[char] = 1
            else:
                needed_chars[char] += 1
        have, need = 0, len(needed_chars)
        start = 0
        for end in range(len(s)):
            current_char = s[end]
            window[current_char] = 1 + window.get(current_char, 0)
            if current_char in needed_chars and needed_chars[current_char] == window[current_char]:
                have += 1

            while have == need:
                if (end - start + 1) < min_substr_len:
                    min_substr_ptr = (start, end)
                    min_substr_len = end - start + 1
                window_start = s[start]
                window[window_start] -= 1
                if window_start in needed_chars and window[window_start] < needed_chars[window_start]:
                    have -= 1
                start += 1
        return s[min_substr_ptr[0]:min_substr_ptr[1] + 1] if min_substr_len != math.inf else ""
