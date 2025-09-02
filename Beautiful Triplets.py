from typing import List


def beautifulTriplets(d: int, arr: List[int]):
    res = 0
    int_count = {}
    for num in arr:
        if int_count.get(num) is None:
            int_count[num] = 1
        else:
            int_count[num] += 1

    arr_set = set(arr)
    for num in arr_set:
        middle = num + d
        end = middle + d
        middle_exists = int_count.get(middle) is not None
        end_exists = int_count.get(end) is not None
        if middle_exists and end_exists:
            res += int_count[num]
    return res