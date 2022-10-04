# Definition for a binary tree node.
from turtle import left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []
        def travers(root):
            if root is None: return
            travers(root.right)
            travers(root.left)
            root.right = self.next
            root.left = None
            self.next = root
        self.next = None
        travers(root)
        return root

test = Solution()
root = TreeNode(1, TreeNode(2))
print(test.flatten(root))