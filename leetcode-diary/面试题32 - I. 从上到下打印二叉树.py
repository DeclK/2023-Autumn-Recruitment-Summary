# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root == None: return []
        stack = collections.deque([root])
        ret = []
        while stack:
            node = stack.popleft()
            ret.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return ret