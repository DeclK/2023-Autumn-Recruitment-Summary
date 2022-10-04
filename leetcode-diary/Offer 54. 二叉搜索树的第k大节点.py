# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 中序遍历第 k 个输出
        count = 0
        ans = None
        def mid(root):
            nonlocal count, ans
            if root == None: return
            if count >= k: return
            mid(root.right)
            count += 1
            if count == k: 
                ans = root.val
                return
            mid(root.left)
        mid(root)
        return ans

test = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(test.kthLargest(root, 5))