# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 对 A 的每一个节点进行遍历，使用中序遍历
        def judge(root, B):
            if B == None:
                return True
            if root and B and root.val == B.val:
                left_ans = judge(root.left, B.left)
                right_ans = judge(root.right, B.right)
                return left_ans and right_ans
            return False

        def traverse(root):
            nonlocal ret
            if root == None:
                return 
            if judge(root, B): 
                ret = True
                return
            traverse(root.left)
            traverse(root.right)
        ret = False
        traverse(A)
        return ret

test = Solution()
A = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
B = TreeNode(3)
print(test.isSubStructure(A, B))