from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            smallest_num = nums[0]
            smallest_num_idx = 0
            for idx in range(len(nums)):
                num = nums[idx]
                if num < smallest_num:
                    smallest_num = num
                    smallest_num_idx = idx
            nums[smallest_num_idx] = smallest_num * multiplier
        return nums
