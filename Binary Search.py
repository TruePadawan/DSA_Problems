import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = math.floor((start + end) / 2)
            middle_el = nums[middle]

            if middle_el == target:
                return middle

            if target < middle_el:
                end = middle - 1
            else:
                start = middle + 1
        return -1
