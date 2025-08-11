from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_map = {}
        sub_boxes = {}
        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[row])):
                # Check for valid rows
                el = board[row][col]
                prev_len = len(row_set)
                row_set.add(el)
                if len(row_set) == prev_len and el != ".":
                    return False

                # Check for valid cols
                if col_map.get(col) is None:
                    col_map[col] = {el}
                else:
                    prev_len = len(col_map[col])
                    col_map[col].add(el)
                    if len(col_map[col]) == prev_len and el != ".":
                        return False

                # Check for valid sub-boxes
                if row <= 2 and col <= 2:
                    if self.isValidSubbox(1, el, sub_boxes) is False:
                        return False
                elif row <= 2 and col <= 5:
                    if self.isValidSubbox(2, el, sub_boxes) is False:
                        return False
                elif row <= 2 and col <= 8:
                    if self.isValidSubbox(3, el, sub_boxes) is False:
                        return False
                elif row <= 5 and col <= 2:
                    if self.isValidSubbox(4, el, sub_boxes) is False:
                        return False
                elif row <= 5 and col <= 5:
                    if self.isValidSubbox(5, el, sub_boxes) is False:
                        return False
                elif row <= 5 and col <= 8:
                    if self.isValidSubbox(6, el, sub_boxes) is False:
                        return False
                elif row <= 8 and col <= 2:
                    if self.isValidSubbox(7, el, sub_boxes) is False:
                        return False
                elif row <= 8 and col <= 5:
                    if self.isValidSubbox(8, el, sub_boxes) is False:
                        return False
                elif row <= 8 and col <= 8:
                    if self.isValidSubbox(9, el, sub_boxes) is False:
                        return False

        return True

    def isValidSubbox(self, index: int, el: str, sub_boxes: dict):
        if sub_boxes.get(index) is None:
            sub_boxes[index] = {el}
        else:
            prev_len = len(sub_boxes[index])
            sub_boxes[index].add(el)
            if len(sub_boxes[index]) == prev_len and el != ".":
                return False
        return True
