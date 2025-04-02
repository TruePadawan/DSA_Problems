from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def backtrack(index: int) -> int:
            if index >= len(questions):
                return 0
            if index in memo:
                return memo[index]
            points = questions[index][0]
            next_index = index + questions[index][1] + 1
            # Choose
            choose_sum = points + backtrack(next_index)
            # Skip
            skip_sum = backtrack(index + 1)

            # cache the max sum at this index
            memo[index] = max(choose_sum, skip_sum)
            return memo[index]
        return backtrack(0)
