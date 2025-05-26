import heapq
import math
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = {}
        heap = []
        heapq.heapify(heap)
        for num in nums:
            if element_count.get(num) is None:
                element_count[num] = 1
            else:
                element_count[num] += 1
        for key, value in element_count.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))
        return list(map(lambda x: x[1], heap))
