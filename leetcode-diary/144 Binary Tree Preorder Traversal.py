from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root != None:
            l.append(root.val)
            l += self.preorderTraversal(root.left)
            l += self.preorderTraversal(root.right)
        return l