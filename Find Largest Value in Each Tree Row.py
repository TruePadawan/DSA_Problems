# Definition for a binary tree node.
import math
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


"""
Use a BFS approach
Keep track of the largest value at each level
"""


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        node_queue = deque([root])
        values = []
        curr_largest_val = -math.inf
        level_size = 1
        while len(node_queue) > 0:
            node = node_queue.popleft()
            level_size -= 1

            if node.val > curr_largest_val:
                curr_largest_val = node.val

            if node.left is not None:
                node_queue.append(node.left)
            if node.right is not None:
                node_queue.append(node.right)

            if level_size == 0:
                level_size = len(node_queue)
                values.append(curr_largest_val)
                curr_largest_val = -math.inf

        return values
