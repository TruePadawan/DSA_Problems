from collections import deque
from typing import List, Tuple

"""
Iterate backwards
Use a stack to maintain elements higher than the current element
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack: deque[Tuple[int, int]] = deque()
        result = [0] * len(temperatures)
        for i in range(len(temperatures), -1, -1):
            temp = temperatures[i]
            while len(temp_stack) > 0 and temp_stack[-1][0] <= temp:
                temp_stack.pop()
            if len(temp_stack) != 0:
                warmer_index = temp_stack[-1][1]
                result[i] = warmer_index - i
            temp_stack.append((temp, i))
        return result
