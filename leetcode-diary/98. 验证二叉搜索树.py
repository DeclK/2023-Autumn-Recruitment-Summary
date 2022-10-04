# Definition for a binary tree node.
from matplotlib.pyplot import flag


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 这比给后序遍历更简单
        def isvalid(root):
            if not root: return True, 1e9, -1e9
            left, l_mini, l_maxi = isvalid(root.left)
            right, r_mini, r_maxi = isvalid(root.right)
            if left and right:
                if r_mini > root.val and l_maxi < root.val:
                    return True, min(l_mini, root.val), max(root.val, r_maxi)
            return False, None, None
        return isvalid(root)[0]

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历
        pre = None
        flag = True
        def travers(root):
            nonlocal pre, flag
            if not root: return
            if not flag: return
            travers(root.left)
            val = root.val
            if pre is not None and val <= pre:
                flag = False
            pre = val
            travers(root.right)
        travers(root)
        return flag

test = Solution()
root = TreeNode(1, TreeNode(-1))
print(test.isValidBST(root))