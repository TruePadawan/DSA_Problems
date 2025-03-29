from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += 0 if i == 0 else nums[i - 1]
        return nums
