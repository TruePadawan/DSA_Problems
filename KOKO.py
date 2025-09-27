import math
from typing import List, Tuple


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The highest pile is guaranteed to be a valid speed
        What about the lowest pile? If it is, what about the next lowest? or second highest?
        What if we use binary search to identify the least pile that is a valid speed
        And another binary search from 0-least_valid_pile
        """
        # Remember their original index
        augmented_piles = sorted([(x, idx) for idx, x in enumerate(piles)])

        i = 0
        j = len(piles) - 1
        least_valid_pile: Tuple[int, int] = (-1, len(piles))
        while i <= j:
            middle = (i + j) // 2
            middle_el = augmented_piles[middle]
            if not self.is_valid(piles, h, middle_el[0]):
                # The current pile is not enough, need something bigger
                i = middle + 1
            else:
                least_valid_pile = middle_el
                j = middle - 1
        i = 1
        j = least_valid_pile[0]

        ans = least_valid_pile[0]
        while i <= j:
            middle = (i + j) // 2
            if not self.is_valid(piles, h, middle):
                i = middle + 1
            else:
                ans = middle
                j = middle - 1

        return ans


    def is_valid(self, piles: List[int], limit: int, speed: int) -> bool:
        eats = 0
        for pile in piles:
            eats += math.ceil(pile / speed)
            if eats > limit:
                return False
        return True