from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def recurse(node: TreeNode) -> bool:
            left_val = False
            right_val = False

            if node.left is not None:
                left_val = recurse(node.left)
            if node.right is not None:
                right_val = recurse(node.right)

            is_leaf_node = node.left is None
            if is_leaf_node:
                return bool(node.val)

            bool_operation = node.val
            if bool_operation == 2:
                return left_val or right_val
            else:
                return left_val and right_val

        return recurse(root)
