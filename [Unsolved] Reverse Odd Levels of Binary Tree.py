# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val, left: TreeNode, right: TreeNode):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        def recurse(node: TreeNode, level: int):
            if node.left is not None:
                level += 1
                recurse(node.left, level)
                recurse(node.right, level)

                if level % 2 != 0:
                    left_val = node.left.val
                    node.left.val = node.right.val
                    node.right.val = left_val

        recurse(root, 0)
        return root
