# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root != None:
            l += self.inorderTraversal(root.left)
            l.append(root.val)
            l += self.inorderTraversal(root.right)
        return l
