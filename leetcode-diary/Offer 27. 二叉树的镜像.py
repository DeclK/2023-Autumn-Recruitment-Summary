# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return 
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(0)
            tempt = node.left
            node.left = node.right
            node.right = tempt
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root