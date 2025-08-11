from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        for i in range(len(nums)):
            left = i
            right = len(nums) - 1 - i

            if left == 0:
                left_products[left] = 1
            else:
                left_products[left] = left_products[left - 1] * nums[left - 1]

            if right == len(nums) - 1:
                right_products[right] = 1
            else:
                right_products[right] = right_products[right + 1] * nums[right + 1]

        for i in range(len(nums)):
            nums[i] = left_products[i] * right_products[i]
        return nums
