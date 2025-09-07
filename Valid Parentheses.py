from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { "(": ")", "{": "}", "[": "]"}
        bracket_stack = deque()
        for char in s:
            is_opening_bracket = brackets.get(char) is not None
            if is_opening_bracket:
                bracket_stack.append(char)
            else:
                # Check that what's at the top of the stack is the opening for the closing bracket
                if len(bracket_stack) > 0 and brackets.get(bracket_stack[-1]) == char:
                    bracket_stack.pop()
                else:
                    return False

        return len(bracket_stack) == 0
            