from typing import List

'''
BRUTE FORCE APPROACH

Iterate clockwise through the gas stations while keeping track of the starting index k
Each iteration is a new starting point
Reset tank and fill it with gas at current starting point
    We're moving to some other station
    subtract the cost from our tank
    if gas left in tank < 0
        go to the next starting point
    else
        add the gas at new station (move to the station)
        If new station is the starting station at index k:
            return k
If the iteration over starting points passes the last station, return -1
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for starting_index in range(len(gas)):
            tank = gas[starting_index]
            # circular_index = 0 if starting_index == len(gas) - 1 else starting_index + 1
            circular_index = starting_index
            while True:
                # Moving to the next station
                tank -= cost[circular_index]
                if tank < 0:
                    # Go to next starting point by breaking out of the loop
                    break
                else:
                    next_station = circular_index + 1 if circular_index <= len(gas) - 2 else 0
                    tank += gas[next_station]
                    circular_index = next_station
                    
                    if circular_index == starting_index:
                        return starting_index
        return -1

test = Solution()
print(test.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))