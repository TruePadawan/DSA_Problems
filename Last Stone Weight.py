"""
We use a max-heap to represent the weight of stones
At each turn:
    If heap length is >= 2:
        we remove the 2 highest weights and smash them
    else:
        if heap length == 1:
            return the only weight remaining
        else:
            return 0
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # simulate a max-heap using a min-heap with negated values
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) >= 2:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            # Smash them
            if a != b:
                heapq.heappush(stones, -(a-b))
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0