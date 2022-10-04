# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        left_in = inorder[:index]
        right_in = inorder[index+1:]

        num_left = len(left_in)
        left_pre = preorder[1: 1+num_left]
        right_pre = preorder[1+num_left:]

        node.left = self.buildTree(left_pre, left_in)
        node.right = self.buildTree(right_pre, right_in)
        return node

test = Solution()
pre = [1,2]; inorder=[2,1]
print(test.buildTree(pre,inorder))