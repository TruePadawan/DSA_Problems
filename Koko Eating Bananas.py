import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        minimum = 0
        while l <= r:
            m = (l+r) // 2
            division_count = 0
            for banana_pile in piles:
                division_count += math.ceil(banana_pile / m)
                if division_count > h:
                    break
            if division_count <= h:
                minimum = m
                r = m - 1
            else:
                l = m + 1
        return minimum