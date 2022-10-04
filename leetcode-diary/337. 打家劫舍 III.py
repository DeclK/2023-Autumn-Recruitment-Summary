# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def sub(root):
            # return 2 status, take or not take
            if not root:
                return 0, 0
            l_take, l_not = sub(root.left)
            r_take, r_not = sub(root.right)
            take_max = l_not + r_not + root.val
            not_max = max(l_take + r_take, l_not + r_take,\
                          l_take + r_not, l_not + r_not)
            return take_max, not_max
        a, b = sub(root)
        return max(a, b)

test = Solution()

