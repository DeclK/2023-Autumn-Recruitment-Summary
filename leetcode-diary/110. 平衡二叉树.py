# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 递归判断
        # 返回高度, 也返回是否为平衡二叉树
        def is_balance(root):
            if not root: return 0, True
            left, l_judge = is_balance(root.left)
            right, r_judge = is_balance(root.right)
            if l_judge and r_judge:
                if abs(left - right) < 1:
                    return max(left, right) + 1, True
            return -1, False
        return is_balance(root)[1]

test = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(test.isBalanced(root))
                
        
        