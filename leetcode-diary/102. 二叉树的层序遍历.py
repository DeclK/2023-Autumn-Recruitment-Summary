# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque()
        if root is None: return
        q.append(root)
        ret = []
        while len(q) > 0:
            cur_layer = []
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                cur_layer.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
            ret.append(cur_layer)
        return ret

test = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
print(test.levelOrder(root))
