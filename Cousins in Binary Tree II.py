from collections import deque
from typing import Optional, List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left: TreeNode, right: TreeNode):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        node_queue = deque([root])
        queue_size = len(node_queue)
        level_sum = {0: 0}
        level = 0

        while len(node_queue) > 0:
            node = node_queue.popleft()
            level_sum[level] += node.val

            if node.left is not None:
                node_queue.append(node.left)
            if node.right is not None:
                node_queue.append(node.right)

            queue_size -= 1
            if queue_size == 0:
                queue_size = len(node_queue)
                level += 1
                level_sum[level] = 0
        new_node_queue: deque[Tuple[TreeNode, Optional[int]]] = deque([(root, None)])
        queue_size = len(new_node_queue)
        level = 0

        while len(new_node_queue) > 0:
            node, sibling_sum = new_node_queue.popleft()

            if sibling_sum is None:
                sibling_sum = node.val

            node.val = level_sum[level] - sibling_sum

            child_sum = 0
            if node.left is not None:
                child_sum += node.left.val
            if node.right is not None:
                child_sum += node.right.val

            if node.left is not None:
                new_node_queue.append((node.left, child_sum))
            if node.right is not None:
                new_node_queue.append((node.right, child_sum))

            queue_size -= 1
            if queue_size == 0:
                queue_size = len(new_node_queue)
                level += 1
        return root
