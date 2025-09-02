import math
from typing import List

"""
Sort the list
Iterate through the list:
    Get the next k-subsets from the current index
    Note the minimum unfairness
"""
def maxMin(k: int, arr: List[int]):
    arr.sort()
    min_diff = math.inf
    for i in range(0, len(arr)):
        if i+k-1 >= len(arr):
            break
        subset = arr[i:i+k]
        unfairness = subset[-1] - subset[0]
        min_diff = min(min_diff, unfairness)
    return min_diff

maxMin(3, [10, 100, 300, 200, 1000, 20, 30])