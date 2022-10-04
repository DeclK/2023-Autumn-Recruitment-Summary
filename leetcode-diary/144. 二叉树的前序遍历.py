# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 需要一个栈来存储状态
        stack = []
        ans = []
        node = root
        while node or stack:    # 这么写是融合了 root == None 的情况
            if node:
                stack.append(node)  # 需要获得其右节点
                ans.append(node.val)  # 前序
                node = node.left
            else:
                node = stack.pop()
                # ans.append(node.val)  # 中序
                node = node.right
        return ans

    def postorder(self, root):
        # 前序 根 -> 右 -> 左的反序
        stack = []
        ans = []
        node = root
        while node or stack:
            if node:
                ans.append(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return ans[::-1]

test = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(test.preorderTraversal(root))
print(test.postorder(root))