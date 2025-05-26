import math
from typing import Optional, List
from collections import deque

"""
Using BFS
Each level has 2^n nodes
The level currently on depends on how many nodes have been visited (k)
Level = log2(k) if result is an int
When we get to a new level, the queue will comprise of all nodes on that level
Make a reverse copy of that
For each node visited, pop the first item and exchange the values
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left: TreeNode, right: TreeNode):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        nodes_visited = 0
        # level = 0 #log2(nodes_visited)
        on_odd_level = False
        node_queue = deque([root])
        node_val_list: List[TreeNode] = []

        while len(node_queue) > 0:
            node = node_queue.popleft()
            nodes_visited += 1
            if math.log2(nodes_visited).is_integer():
                # level = math.log2(nodes_visited)
                on_odd_level = math.log2(nodes_visited) % 2 != 0
                if on_odd_level:
                    node_val_list = list(map(lambda x: x.val, node_queue))
                    node_val_list.insert(0, node.val)

            if on_odd_level:
                new_val = node_val_list.pop()
                node.val = new_val

            if node.left is not None:
                node_queue.append(node.left)
                node_queue.append(node.right)
        return root


print(math.log2(8))
