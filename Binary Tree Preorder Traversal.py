from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val= 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_stack = [root]
        processed_nodes = []
        while len(node_stack) > 0:
            node = node_stack.pop()
            if node is None:
                break
            processed_nodes.append(node.val)
            if node.right is not None:
                node_stack.append(node.right)
            if node.left is not None:
                node_stack.append(node.left)
        return processed_nodes
