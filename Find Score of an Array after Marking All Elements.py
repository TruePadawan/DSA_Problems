from typing import List

"""
keep track of marked scores in a boolean array
loop
get the index of the smallest unmarked score
mark it and its adjacent scores
score += small number
"""


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked_nums = [False] * len(nums)
        sorted_unmarked_scores = sorted([(num, index) for index, num in enumerate(nums)])

        for i in range(len(nums)):
            smallest_unmarked_index = sorted_unmarked_scores[i][1]
            smallest_unmarked_score = sorted_unmarked_scores[i][0]
            
            if marked_nums[smallest_unmarked_index] is False:
                score += smallest_unmarked_score
            
                left_index = smallest_unmarked_index - 1
                right_index = smallest_unmarked_index + 1
                marked_nums[smallest_unmarked_index] = True

                if smallest_unmarked_index > 0 and marked_nums[left_index] is False:
                    marked_nums[left_index] = True

                if right_index < len(nums) and marked_nums[right_index] is False:
                    marked_nums[right_index] = True

        return score


solution = Solution()
print(
    solution.findScore(
        [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]
    )
)