# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


"""
In order traversal of a BST gives a sorted array
Get the minimum abs diff between adjacent values
"""


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sorted_list = []

        def inorder_traversal(root: TreeNode):
            if root.left is not None:
                inorder_traversal(root.left)
            sorted_list.append(root.val)
            if root.right is not None:
                inorder_traversal(root.right)

        inorder_traversal(root)

        min_diff = math.inf
        for i in range(len(sorted_list)):
            if i + 1 >= len(sorted_list):
                break
            diff = abs(sorted_list[i] - sorted_list[i + 1])
            if diff < min_diff:
                min_diff = diff
            if min_diff == 1:
                break
        return min_diff
