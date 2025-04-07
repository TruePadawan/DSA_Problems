# https://leetcode.com/problems/maximum-strength-of-a-group/description/

from functools import reduce
from typing import List

"""
Split the array into positive and negative numbers
Sort the negative numbers list and make it contain an even amount of numbers:
    Get rid of the "higher" negative numbers first
Once the length of negative numbers list is even:
    Find the product of all remaining negative and positive numbers
"""


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        positive_arr, negative_arr = self.split_arr(nums)
        while len(negative_arr) % 2 != 0:
            negative_arr.pop()

        if positive_arr.count(0) == len(positive_arr):
            # All values are 0
            if len(negative_arr) == 0:
                return 0
            else:
                return reduce(lambda x, y: x * y, negative_arr, 1)
        else:
            while positive_arr.count(0) != 0:
                positive_arr.remove(0)
            return reduce(lambda x, y: x * y, positive_arr, 1) * reduce(lambda x, y: x * y, negative_arr, 1)

    def split_arr(self, nums: List[int]):
        negative_arr = []
        nums.sort()
        splice_index = 0
        for index, num in enumerate(nums):
            # if num == 0:
            #     splice_index = index+1
            #     continue
            if num >= 0:
                break
            negative_arr.append(num)
            splice_index = index+1
        nums = nums[splice_index:]
        return [nums, negative_arr]