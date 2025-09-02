import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res = []
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, (-nums[i], i))
                if len(heap) == k:
                    res.append(self.get_largest(heap, (i - k + 1, i)))
            else:
                heapq.heappush(heap, (-nums[i], i))
                res.append(self.get_largest(heap, (i-k+1, i)))
        return res
    def get_largest(self, heap: List[int], bound: tuple[int, int]) -> int:
        num, index = heap[0]
        while index < bound[0]:
            heapq.heappop(heap)
            num, index = heap[0]
        return -num

soln = Solution()
soln.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)