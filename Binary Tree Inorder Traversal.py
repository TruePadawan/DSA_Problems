from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        processed_nodes = []
        if root is None:
            return processed_nodes

        def recurse(node: TreeNode):
            if node.left is not None:
                recurse(node.left)
            processed_nodes.append(node.val)
            if node.right is not None:
                recurse(node.right)

        recurse(root)

        return processed_nodes
