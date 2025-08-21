from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        left = 0
        right = len(height) - 1
        while left < right:
            breadth = right - left
            length = min(height[left], height[right])
            area = breadth * length
            if area > max_amount:
                max_amount = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_amount
