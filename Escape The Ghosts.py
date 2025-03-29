from typing import List

'''
Let's find the minimum number of moves needed to get to the target
If the number of moves needed for any of the ghosts to get to the target is <= the number of moves needed for the player to get to the target:
    then the player will be caught
else:
    the player will escape
'''

'''
If a ghost or person is at (x, y) and the target is at (tx, ty), then the number of moves needed to get to the target is: |x - tx| + |y - ty|
'''

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_min_number_of_moves = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            ghost_min_number_of_moves = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_min_number_of_moves <= my_min_number_of_moves:
                return False
        return True