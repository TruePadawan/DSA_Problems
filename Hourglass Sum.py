import math
from typing import List


def hourglassSum(arr: List[List[int]]):
    max_sum = -math.inf
    for i in range(2, len(arr)):
        for j in range(2, len(arr[i])):
            top = arr[i - 2]
            middle = arr[i - 1]
            bottom = arr[i]

            top_sum = top[j - 2] + top[j - 1] + top[j]
            middle_sum = middle[j - 1]
            bottom_sum = bottom[j - 2] + bottom[j - 1] + bottom[j]

            hourglass_sum = top_sum + middle_sum + bottom_sum
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    return max_sum
