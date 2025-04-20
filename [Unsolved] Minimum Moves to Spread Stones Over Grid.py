from collections import deque
from typing import List

"""
Loop through the grid, if a cell with more than 1 stone is found:
    Add it to the queue
For each cell in the queue:
    Possible approach 1:
        share its stones to adjacent sides with less stones until only 1 left,
        increment number of moves by 1
        each side that has more than 1 stone will be added to the queue
        do this until the queue is empty
"""


def get_sides_with_less_stones(grid: List[List[int]], cell: tuple[int, int]):
    cell_stones = grid[cell[0]][cell[1]]
    valid_sides = []

    top_side_cell = (cell[0] - 1, cell[1])
    down_side_cell = (cell[0] + 1, cell[1])
    left_side_cell = (cell[0], cell[1] - 1)
    right_side_cell = (cell[0], cell[1] + 1)
    # top side cell is valid
    if top_side_cell[0] >= 0:
        if grid[top_side_cell[0]][top_side_cell[1]] == 0:
            valid_sides.append(top_side_cell)
    # downwards cell is valid
    if down_side_cell[0] <= 2:
        if grid[down_side_cell[0]][down_side_cell[1]] == 0:
            valid_sides.append(down_side_cell)
    # leftwards cell is valid
    if left_side_cell[1] >= 0:
        if grid[left_side_cell[0]][left_side_cell[1]] == 0:
            valid_sides.append(left_side_cell)
    # rightwards cell is valid
    if right_side_cell[1] <= 2:
        if grid[right_side_cell[0]][right_side_cell[1]] == 0:
            valid_sides.append(right_side_cell)
    return valid_sides


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        moves = 0
        cell_queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = (i, j)
                if grid[i][j] == 1 or grid[i][j] == 0:
                    continue
                cell_queue.append(cell)
        while len(cell_queue) > 0:
            cell = cell_queue.popleft()
        # for cell in cell_queue:
            i, j = cell
            valid_sides = get_sides_with_less_stones(grid, cell)
                # valid_sides = self.get_sides_with_less_stones(grid, cell)
            while grid[i][j] != 1:
                for side in valid_sides:
                    if grid[i][j] == 1:
                        # cell_queue.popleft()
                        break
                    grid[side[0]][side[1]] += 1
                    grid[i][j] -= 1
                    if grid[side[0]][side[1]] > 1:
                        cell_queue.append(side)
                    # valid_sides.pop(0)
                    # valid_sides.append(side)
                    moves += 1
        return moves


soln = Solution()
print(soln.minimumMoves([[1,1,0],[1,1,1],[1,2,1]]))