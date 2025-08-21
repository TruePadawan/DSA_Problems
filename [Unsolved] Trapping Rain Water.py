from typing import List

"""
The amount of water trapped depends on both sides not just one, there has to be a "barrier" (two highs)
A "high" starts from 1

When we dip after a high, add the diff between the current highest height and the dip height to the count

It stops being a dip when we reach a height that is >= prev highest height
OR
Increase in height then a dip

Queue adding the counts until after a new max height is reached
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = i + 1
        operations = []
        dip = False
        amount = 0
        # highest_height = -1
        while j < len(height):
            if not dip and height[i] <= height[j]:
                i += 1
                j += 1
                continue
            if not dip and height[j] < height[i]:
                dip = True
                # highest_height = i
                operations.append((height[i] - height[j], j))
                # amount += height[i] - height[j]
                j += 1
                continue
            if dip and height[j] <= height[i]:
                operations.append((height[i] - height[j], j))
                # amount += height[i] - height[j]
                j += 1

                if height[j - 1] > height[j]:
                    dip = False
                    width = j - i - 1
                    length = height[i] - height[j - 1]
                    operations.append((-(width*length), j))
                    # amount -= width * length
                    i = j - 1
                continue
            if dip and height[j] > height[i]:
                # highest_height = j
                i = j
                j += 1
                dip = False
                continue
        for val, index in operations:
            if index <= i or val < 0:
                # print(val, index)
                amount += val
        # print(amount)
        return amount


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         elevation_pairs = []
#         i = 0
#         j = i + 1
#         dip = False
#         while j < len(height):
#             if not dip and height[i] <= height [j]:
#                 i += 1
#             elif not dip and height[j] < height[i]:
#                 dip = True
#             elif dip and height[j] < height[j - 1]:
#                 i = j - 1
#             elif dip and height[j] >= height[i]:
#                 elevation_pairs.append((i, j))
#                 i = j
#                 dip = False
#             j += 1
#         print(elevation_pairs)
#         return 0

soln = Solution()
soln.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
