from typing import List

# [5,6,7,8,9,12,15,17]
"""
Sort the array and while using binary search:
    Check if middle element can be allocated k times:
        If it can't then nothing above it can
            Focus on elements below it
        If it can:
            Focus on elements after it
        Return the largest number that can be allocated k times
        Return 0 if no number can be allocated k times
"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()

        sub_piles = list(range(1, candies[-1]+1))
        largest = 0
        l = 0
        r = len(sub_piles) - 1
        while l <= r:
            m = (l + r) // 2
            candy = sub_piles[m]
            if self.can_be_allocated_k_times(candies, candy, k):
                largest = sub_piles[m]
                l = m + 1
            else:
                r = m - 1
        return largest

    def can_be_allocated_k_times(self, candies: List[int], candy: int, k: int):
        division_count = 0
        for item in reversed(candies):
            if item < candy:
                break
            division_count += item // candy
            if division_count >= k:
                return True
        return False


soln = Solution()
soln.maximumCandies([9, 10, 1, 2, 10, 9, 9, 10, 2, 2], 3)