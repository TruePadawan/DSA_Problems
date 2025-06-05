from typing import List, Optional

"""
Create a tree structure from the data
    Each node's value will be the inform time
DFS through the tree
Pick the max time at each subtree
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        class TreeNode:
            def __init__(self, inform_time=0):
                self.inform_time = inform_time
                self.children: list[int] = []

        # Create tree-like structure from manager data
        tree: dict[int, TreeNode] = {}
        for i in range(len(manager)):
            m = manager[i]
            if m == -1 and tree.get(headID) is None:
                tree[headID] = TreeNode(informTime[headID])
                continue
            if tree.get(m) is None:
                node = TreeNode(informTime[m])
                node.children = [i]
                tree[m] = node
            else:
                tree[m].children.append(i)

        def recurse(tree_node: TreeNode):
            max_inform_time = 0
            for child in tree_node.children:
                child_node = tree.get(child)
                if child_node is not None:
                    if len(child_node.children) == 0:
                        continue
                    inform_time = recurse(tree[child])
                    if inform_time > max_inform_time:
                        max_inform_time = inform_time
            return tree_node.inform_time + max_inform_time

        time_taken = recurse(tree[headID])
        return time_taken