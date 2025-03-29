import math
from typing import List

"""
Basically find the smallest number and the largest number that comes after it
return 0 if no larger number after it (smallest number is at the end of the list)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        smallest = math.inf
        largest = -math.inf
        max_profit = 0
        for i in range(len(prices)):
            at_end_of_list = i == len(prices) - 1
            if at_end_of_list:
                break

            current_cost = prices[i]
            next_cost = prices[i + 1]
            if current_cost < smallest:
                smallest = current_cost
                largest = -math.inf
            if next_cost > largest:
                largest = next_cost
            if largest - smallest > max_profit:
                max_profit = largest - smallest
        return max_profit
