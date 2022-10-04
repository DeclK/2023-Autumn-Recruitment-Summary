# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 深度搜索
        ans = []
        path = []
        def dfs(node, target):
            nonlocal path
            if not node: return
            path.append(node.val)
            if node.left == node.right == None and target == node.val:
                ans.append(path[:])
                path.pop()
                return
            dfs(node.left, target - node.val)
            dfs(node.right, target - node.val)
            path.pop()
            
        dfs(root, targetSum)
        return ans