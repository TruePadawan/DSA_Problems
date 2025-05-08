from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # tree_str = ""
        # processed_nodes = []
        if root is None:
            return ""
        def recurse(node: TreeNode) -> str:
            # processed_nodes.append(node.val)
            left_str = ""
            right_str = ""
            if node.left is not None:
                left_str = recurse(node.left)
            if node.right is not None:
                right_str = recurse(node.right)

            has_only_right_node = left_str == "" and right_str != ""
            if has_only_right_node:
                left_str = "()"
            has_no_child_node = left_str == "" and right_str == ""
            if has_no_child_node:
                return f"({node.val})"
            else:
                return f"({node.val}{left_str}{right_str})"
        result = recurse(root)
        result = result[1:len(result)-1]
        return result