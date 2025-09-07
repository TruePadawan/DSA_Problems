from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        brackets = { "(": ")" }
        bracket_stack = deque()
        indices = [0] * len(s)

        for i in range(len(s)):
            char = s[i]
            is_opening_bracket = brackets.get(char) is not None
            if is_opening_bracket:
                bracket_stack.append((char, i))
            else:
                # Check that what's at the top of the stack is the opening for the closing bracket
                if len(bracket_stack) > 0 and brackets.get(bracket_stack[-1][0]) == char:
                    opening_brace = bracket_stack.pop()
                    indices[opening_brace[1]] = 1
                    indices[i] = 1

        longest = 0
        count = 0
        for i in range(len(indices)):
            num = indices[i]
            if num == 1:
                count += 1
                longest = count if count > longest else longest
            else:
                count = 0
        return longest

soln = Solution()
print(
    soln.longestValidParentheses("((()))())")
)