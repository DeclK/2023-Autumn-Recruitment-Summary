# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return
        def get_sum(l):
            ret = 0
            for node in l:
                ret += node.val
            return ret
            
        stack = [root]
        maxinum = -1e7
        ret = None
        layer = 1
        while stack:
            summ = get_sum(stack)
            if summ > maxinum:
                ret = layer
                maxinum = summ
            layer += 1
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        
        return ret

test = Solution()
root = TreeNode(1, TreeNode(7), TreeNode(0))
print(test.maxLevelSum(root))
