from typing import List
'''
--ALGORITHM LOGIC--
Loop through the array - i
If current element is 0
    keep track of it's index - j
    sliding window technique shows that the number of subarrays in the subset of size n will be n + (n-1) + (n-2) ... 1
    at each subsequent loop, increment occurrence of 0-subarray by the size of the subset between i and j (i-j+1)
reset j when current element is not 0
'''



class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        occurrences = 0
        i = 0
        j = -2
        while i < len(nums):
            if nums[i] == 0 and j == -2:
                j = i
                occurrences += 1
            elif nums[i] == 0 and j != -2:
                subset_size = i - j + 1
                occurrences += subset_size
            elif nums[i] != 0:
                j = -2
            i += 1
        return int(occurrences)


test = Solution()
print(int(test.zeroFilledSubarray([1,3,0,0,2,0,0,4])))