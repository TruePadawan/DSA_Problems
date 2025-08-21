from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1
        res = [0, 0]
        while left_ptr < right_ptr:
            one = numbers[left_ptr]
            two = numbers[right_ptr]
            _sum = one + two
            if _sum == target:
                res = [left_ptr+1, right_ptr+1]
                break
            elif _sum < target:
                left_ptr += 1
            else:
                right_ptr -= 1
        return res