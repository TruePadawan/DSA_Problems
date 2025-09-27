from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = deque()
        for token in tokens:
            if token.isdigit() or token[0] == "-" and token[1:].isdigit():
                num_stack.append(int(token))
            else:
                r_operand = num_stack.pop()
                l_operand = num_stack.pop()
                if token == "+":
                    num_stack.append(l_operand + r_operand)
                elif token == "-":
                    num_stack.append(l_operand - r_operand)
                elif token == "*":
                    num_stack.append(l_operand * r_operand)
                else:
                    num_stack.append(int(l_operand / r_operand))
        return num_stack.pop()
