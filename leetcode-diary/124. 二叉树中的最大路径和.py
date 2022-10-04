# Definition for a binary tree node.
from decimal import Subnormal
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 动态规划在树结构当中的应用
        # 以某个节点为根节点的最大路径和
        # 需要增加状态, 还需要字根
        ans = -1e9
        def maxpathsum(root):
            nonlocal ans
            if not root: return -1e9
            left_max = maxpathsum(root.left)
            right_max = maxpathsum(root.right)
            sub_only = max(root.val, root.val + left_max, root.val + right_max)
            ans = max(ans, sub_only, root.val + left_max + right_max)
            return sub_only
        maxpathsum(root)
        return ans

test = Solution()
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(test.maxPathSum(root))