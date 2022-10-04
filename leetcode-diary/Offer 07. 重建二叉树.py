# Definition for a binary tree node.
from bisect import insort_right
import enum
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx_mid = inorder.index(preorder[0])
        left_inorder = inorder[:idx_mid]
        right_inorder = inorder[idx_mid + 1:]

        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

# mark 2
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # recursive building 
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right: return
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            # 查询还可以使用 哈希 进一步优化
            in_pos = inorder[in_left: in_right + 1].index(root_val) + in_left

            in_left1 = in_left
            in_right1 = in_pos - 1
            in_left2 = in_pos + 1
            in_right2 = in_right

            pre_left1 = pre_left + 1
            pre_right1 = pre_left1 + (in_right1 - in_left1)
            pre_left2 = pre_right1 + 1
            pre_right2 = pre_right
            root.left = build(pre_left1, pre_right1, in_left1, in_right1)
            root.right = build(pre_left2, pre_right2, in_left2, in_right2)
            return root
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
test = Solution()
print(test.buildTree(preorder, inorder))