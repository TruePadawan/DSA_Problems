#  https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/
from typing import List

"""
We can start drinking for either A or B
After picking a starting point, at each stage we can:
- Drink from the currently selected energy drink
- Choose the other energy drink but at a cost of 1 hr
At each stage, we want what gives us the maximum energy
"""


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        max_hours = len(energyDrinkA)
        memo1 = {}
        memo2 = {}

        def backtrack(initial_energy_drink: List[int], other_energy_drink: List[int], hour: int, selecting_from_a: bool):
            if hour >= max_hours:
                return 0
            if selecting_from_a:
                if hour in memo1:
                    return memo1[hour]
            else:
                if hour in memo2:
                    return memo2[hour]

            energy = initial_energy_drink[hour]
            # Drink from the currently selected energy drink
            energy_gained_from_drinking = energy + backtrack(initial_energy_drink, other_energy_drink, hour + 1, selecting_from_a)
            # Choose to drink from the other energy drink, it costs 1 hr
            energy_gained_from_skipping = backtrack(other_energy_drink, initial_energy_drink, hour + 1, not selecting_from_a)

            max_energy_gained = max(energy_gained_from_drinking, energy_gained_from_skipping)
            if selecting_from_a:
                memo1[hour] = max_energy_gained
            else:
                memo2[hour] = max_energy_gained
            return max_energy_gained

        energy_gained_starting_from_A = backtrack(energyDrinkA, energyDrinkB, 0, True)
        energy_gained_starting_from_B = backtrack(energyDrinkB, energyDrinkA, 0, False)
        return max(energy_gained_starting_from_A, energy_gained_starting_from_B)