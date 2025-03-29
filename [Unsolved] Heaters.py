from typing import List

'''
For each house, calculate the distance to the closest heater
The largest distance from a house to its closest heater is the min radius needed to satisfy all houses
'''

'''
A brute-force approach
Correct but exceeds the time limit for large test cases
'''
# class Solution:
#     def findRadius(self, houses: List[int], heaters: List[int]) -> int:
#         distances_from_house_to_closest_heater = []
#         for i in range(1, len(houses)):
#             min_distance = abs(heaters[0] - houses[0])
#             for j in range(1, len(heaters)):
#                 distance = abs(heaters[j] - houses[i])
#                 if distance < min_distance:
#                     min_distance = distance
#             distances_from_house_to_closest_heater.append(min_distance)
#         distances_from_house_to_closest_heater.sort()
#         return distances_from_house_to_closest_heater[-1]

'''
An efficient approach using binary search to find heater closest to a house
'''

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        largest_distance = float('-inf')
        houses.sort()
        heaters.sort()
        
        for house in houses:
            heater = self.findClosestHeater(house, heaters)
            min_distance = abs(house - heater)
            if min_distance > largest_distance:
                largest_distance = min_distance
        return largest_distance
    
    def findClosestHeater(self, house: int, heaters: List[int]) -> int:
        left = 0
        right = len(heaters) - 1
        while left < right:
            if right - left == 1: # If the length is 2
                distance1 = abs(heaters[left] - house)
                distance2 = abs(heaters[right] - house)
                if distance1 < distance2:
                    return heaters[left]
                else:
                    return heaters[right]
            mid = (left + right) // 2
            if heaters[mid] < house:
                left = mid + 1
            elif heaters[mid] == house:
                return heaters[mid]
            else:
                right = mid
        return heaters[left]
    

test = Solution()
print(test.findRadius([1,2,3,4], [1,4]))