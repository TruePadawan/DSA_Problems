from typing import List


def bubble_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    arr_sorted = False
    i = 1
    swap_done = False
    while not arr_sorted:
        if arr[i] < arr[i - 1]:
            temp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = temp
            swap_done = True
        i += 1
        if i == len(arr):
            i = 1
            arr_sorted = swap_done == False
            swap_done = False
    return arr


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            else:
                break
    return arr


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    smaller_els = list(filter(lambda x: x <= pivot, arr))
    larger_els = list(filter(lambda x: x > pivot, arr))

    part_1 = quick_sort(smaller_els)
    part_2 = quick_sort(larger_els)

    part_1.append(pivot)
    part_1.extend(part_2)

    return part_1


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    middle_idx = len(arr) // 2
    l_arr = arr[:middle_idx]
    r_arr = arr[middle_idx:]

    sorted_left = merge_sort(l_arr)
    sorted_right = merge_sort(r_arr)
    final_arr = []

    l, r = 0, 0
    while l < len(sorted_left) or r < len(sorted_right):
        if l < len(sorted_left) and r < len(sorted_right):
            if sorted_left[l] < sorted_right[r]:
                final_arr.append(sorted_left[l])
                l += 1
            else:
                final_arr.append(sorted_right[r])
                r += 1
        else:
            if l < len(sorted_left):
                final_arr.append(sorted_left[l])
                l += 1
            elif r < len(sorted_right):
                final_arr.append(sorted_right[r])
                r += 1
    return final_arr

def merge_and_sort(A: List[int], B: List[int]) -> List[int]:
    sorted_a = quick_sort(A)
    sorted_b = quick_sort(B)

    pointer_a, pointer_b = 0, 0
    result = []
    while pointer_a < len(sorted_a) or pointer_b < len(sorted_b):
        if pointer_a < len(sorted_a) and pointer_b < len(sorted_b):
            if sorted_a[pointer_a] < sorted_b[pointer_b]:
                result.append(sorted_a[pointer_a])
                pointer_a += 1
            else:
                result.append(sorted_b[pointer_b])
                pointer_b += 1
        else:
            if pointer_a < len(sorted_a):
                result.append(sorted_a[pointer_a])
                pointer_a += 1
            else:
                result.append(sorted_b[pointer_b])
                pointer_b += 1
    return result

print(merge_and_sort([2,3,4,5], [1,6,8,7]))