# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root is None: return
        stack = [root]
        count = 1
        while stack:
            if count == depth:
                for node in stack:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(val)
                    node.left.left = left
                    node.right = TreeNode(val)
                    node.right.right = right
                break
            else:
                new_stack = []
                for node in stack:
                    if node.left:
                        new_stack.append(node.left)
                    if node.right:
                        new_stack.append(node.right)
                stack = new_stack
                count += 1
        return root

test = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
test.addOneRow(root, -1, 1)
print(-1)