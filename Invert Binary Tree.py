# Definition for a binary tree node.
from typing import Optional

"""
Recursively go through the left node until current node has no left node
[I assume that if no left node, then no right]
Go to the parent node -> Swap the child nodes
Then do the same for the right node of the parent node
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.invertTree(root=root.left)
        self.invertTree(root=root.right)

        saved_left_node = root.left
        root.left = root.right
        root.right = saved_left_node

        return root
