# https://leetcode.com/problems/maximum-spending-after-buying-items/
import math
from typing import List

"""
We essentially want to sacrifice smaller ds, we want to pair low ds with low values
So that we can pair large ds with larger values.

So basically, on each day:
 Pair d with the smallest available rightmost value
 
Do this so larger ds can be paired with larger values
"""


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        max_amount_spent = 0
        selected_items_tracker: dict[int, int] = {}
        num_of_shops = len(values)
        num_of_items_per_shop = len(values[0])
        days_count = num_of_shops * num_of_items_per_shop

        for ith_day in range(1, days_count + 1):
            smallest_rightmost_item = {"ith_shop": math.inf, "value": math.inf}
            # Select the smallest rightmost value that is available per shop
            for j in range(num_of_shops):
                shop = values[j]
                # How many items have I already selected from this shop?
                selected_items_count = selected_items_tracker.get(j)
                index = num_of_items_per_shop - 1
                if selected_items_count is not None:
                    index = (num_of_items_per_shop - 1) - selected_items_count
                if index >= 0 and shop[index] < smallest_rightmost_item["value"]:
                    smallest_rightmost_item = {"ith_shop": j, "value": shop[index]}

            selected_shop = int(smallest_rightmost_item["ith_shop"])
            value = smallest_rightmost_item["value"]
            if selected_items_tracker.get(selected_shop) is None:
                selected_items_tracker[selected_shop] = 1
            else:
                selected_items_tracker[selected_shop] += 1
            max_amount_spent += value * ith_day

        return max_amount_spent
