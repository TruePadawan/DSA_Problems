from typing import List

"""
Essentially we have to do 2 binary searches
One going through the rows looking for a bound where target could be
If found:
    Do another binary search looking for target, return true if found else false
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i <= j:
            middle =  (i+j) // 2
            middle_row = matrix[middle]
            # Check that target is within bounds
            if target < middle_row[0]:
                # Ignore rows to the right of the current row
                j = middle - 1
            elif target > middle_row[-1]:
                # Ignore rows to the left of the current row
                i = middle + 1
            else:
                # Binary search throw this current row
                return self.binary_search(middle_row, target)
        return False
    def binary_search(self, arr: List[int], target: int) -> bool:
        i = 0
        j = len(arr) - 1
        while i <= j:
            middle =  (i+j) // 2
            middle_el = arr[middle]
            if target < middle_el:
                j = middle - 1
            elif target > middle_el:
                i = middle + 1
            else:
                return True
        return False