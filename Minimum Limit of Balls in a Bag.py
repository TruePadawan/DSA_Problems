import math
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        min_maximal_value = 1
        l = 1
        r = max(nums)
        while l <= r:
            m = (l+r) // 2
            is_valid_maximal_value = True
            operations_count = 0
            for bag in nums:
                operations_count += math.ceil(bag / m) - 1
                if operations_count > maxOperations:
                    is_valid_maximal_value = False
                    break
            if is_valid_maximal_value:
                min_maximal_value = m
                r = m - 1
            else:
                l = m + 1
        return min_maximal_value



soln = Solution()
print(soln.minimumSize([7, 17], 2))
