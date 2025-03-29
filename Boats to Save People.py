from typing import List

"""
Solved via tip from Anuron Das
https://leetcode.com/problems/boats-to-save-people/description/comments/1852302

sort the list of weights
remove all the people with weights == limit, they will have one boat
have two pointers at min and max
if max + min weight > limit
    max can't be paired with anyone else, so it will have one boat,
    move to next max weight
else pair current max and min weight in one boat
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        boats = 0
        people.sort()

        max_index = len(people) - 1
        min_index = 0
        while max_index >= min_index:
            if people[max_index] == limit:
                # Remove people whose weight == limit
                boats += 1
            elif max_index == 0:
                boats += 1
                break
            elif people[max_index] + people[min_index] > limit:
                boats += 1
            else:
                boats += 1
                min_index += 1
            max_index -= 1
        return boats


test = Solution()
print(test.numRescueBoats([3, 2, 2, 1], 3))
