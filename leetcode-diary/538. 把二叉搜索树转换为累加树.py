# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.tree_vals = []
        self.tree_nodes = []
        def travers(root):
            if not root: return
            travers(root.left)
            self.tree_vals.append(root.val)
            self.tree_nodes.append(root)
            travers(root.right)

        travers(root)
        accumulate_sum = []
        n = len(self.tree_vals)
        for idx in range(n - 1, -1, -1):
            if idx == n - 1:
                accumulate_sum.append(self.tree_vals[idx])
                continue
            accumulate_sum.append(self.tree_vals[idx] + accumulate_sum[-1])
        accumulate_sum = accumulate_sum[::-1]
        
        for node, val in zip(self.tree_nodes, accumulate_sum):
            node.val = val
        return root
