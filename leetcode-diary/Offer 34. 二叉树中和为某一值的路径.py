# Definition for a binary tree node.
from turtle import left
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans = []
        def dfs(node, path, target):
            if node and node.left == node.right == None:
                if target == node.val:
                    ans.append(path + [node.val])
                return
            if node.left: 
                dfs(node.left, path + [node.val], target - node.val)
            if node.right:
                dfs(node.right, path + [node.val], target - node.val)
        if root == None:
            return []
        dfs(root, [], target)
        return ans

test = Solution()
root = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), 
                TreeNode(-3, TreeNode(-2)))
target = -1
print(test.pathSum(root, target))