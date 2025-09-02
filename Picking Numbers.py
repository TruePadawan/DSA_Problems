from typing import List

"""
Brute force could probably work given the constraints of the problem (n <= 100)

Alternative approach (sliding window):
Starting from the beginning of the list:
    Increase window if the abs diff between the first value in the window and the next value is <= 1
        Consider this the next starting point
    If the abs diff is > 1 or at last value in the list:
        note the current size of the window
        move to the next starting point
"""
def pickingNumbers(a: List[int]):
    if len(a) <= 1:
        return len(a)
    start = 0
    end = 0
    next_start = -1
    max_subarray_len = 0
    # This approach requires the list to be sorted
    a.sort()
    while end < len(a):
        if a[end] != a[start] and next_start == -1:
            next_start = end
        if abs(a[start] - a[end]) <= 1:
            end += 1
            if end == len(a):
                subarray_len = end - start
                max_subarray_len = max(max_subarray_len, subarray_len)
        else:
            subarray_len = end - start
            max_subarray_len = max(max_subarray_len, subarray_len)
            start = next_start if next_start != -1 else end
            # end += 1
            next_start = -1
    return max_subarray_len