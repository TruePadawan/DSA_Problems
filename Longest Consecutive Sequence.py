from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = {}
        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return 1
        longest_len = 1 if len(nums) >= 1 else 0
        for num in nums:
            if consecutive.get(num - 1) is None:
                consecutive[num] = [num]
            else:
                master_ref = consecutive[num - 1]
                if isinstance(master_ref, int):
                    consecutive[master_ref].append(num)
                    if len(consecutive[master_ref]) > longest_len:
                        longest_len = len(consecutive[master_ref])
                else:
                    consecutive[num - 1].append(num)
                    if len(consecutive[num - 1]) > longest_len:
                        longest_len = len(consecutive[num - 1])
                consecutive[num] = consecutive[num - 1]
        return longest_len
