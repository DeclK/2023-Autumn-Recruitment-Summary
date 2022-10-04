# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(head_1, head_2):
            if head_1 is None and head_2 is None: return True
            if head_1 is None: return False
            if head_2 is None: return False
            if head_1.val != head_2.val: return False
            return check(head_1.left, head_2.right) and \
                    check(head_1.right, head_2.left)
        return check(root, root)
            
test = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(2))
print(test.isSymmetric(root))