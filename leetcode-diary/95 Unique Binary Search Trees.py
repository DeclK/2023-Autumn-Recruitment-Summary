# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def g(start, end):
            if start > end:
                return [None]
            ret = []
            for i in range(start, end + 1):
                # i += 1
                left_tree_list = g(start, i - 1)
                right_tree_list  = g(i + 1, end)
                for left in left_tree_list:
                    for right in right_tree_list:
                        root = TreeNode(val=i)
                        root.left = left
                        root.right = right
                        ret.append(root)
            return ret
        return g(1, n)


test = Solution()
test.generateTrees(3)
# print(test.generateTrees(1))