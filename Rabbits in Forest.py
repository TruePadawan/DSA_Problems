from typing import List

"""
Use a dict to keep track of number of rabbits with the same colors
For each ith answer, there is at minimum anwers[i] + 1 rabbits with same color
loop through the list, for each answer (answer[i]):
    if it's not in the dict or if it is in the dict but its value is 0:
        pair it with answer[i] + 1
        increment the min number of rabbits by answers[i] + 1
        decrement its value by 1
    else if it is in the dict but its value is not 0:
        decrement its value by 1
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = {}
        minRabbits = 0
        for count in answers:
            if rabbits.get(count) is None or rabbits.get(count) == 0:
                rabbits[count] = count + 1
                minRabbits += count + 1
                rabbits[count] -= 1
            elif rabbits.get(count) > 0:
                rabbits[count] -= 1
        return minRabbits
