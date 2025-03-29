from functools import reduce
import math
from typing import List

'''
sort the list and pick the largest
update the largest with its floored square root
re-do the above k amount of times
sum up the list
'''
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        giftsCopy = gifts.copy()
        for i in range(k):    
            giftsCopy.sort()
            largest_pile = giftsCopy[-1]
            floored_root = math.floor(math.sqrt(largest_pile))
            giftsCopy[-1] = floored_root
        return reduce(lambda x, y: x+y, giftsCopy)
            