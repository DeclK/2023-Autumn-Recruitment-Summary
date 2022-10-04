# Definition for a binary tree node.
from math import fabs


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        flag = True
        def traverse(root, depth):
            nonlocal flag
            if root == None: return depth - 1
            left = traverse(root.left, depth + 1)
            if flag == False: return
            right = traverse(root.right, depth + 1)
            if flag == False: return
            if flag and abs(left - right) > 1: 
                flag = False
            return max(left, right)
        traverse(root, 1)
        return flag

test = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
root = TreeNode(3, TreeNode(1, None, TreeNode(2)))
print(test.isBalanced(root))