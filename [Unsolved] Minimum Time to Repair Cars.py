from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        max_time = max(ranks) * (cars ** 2)
