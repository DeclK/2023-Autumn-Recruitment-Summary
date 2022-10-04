# Definition for a binary tree node.
from logging.handlers import WatchedFileHandler
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归就 vans 了
        if root == None:
            return True
        def is_sym(left, right):
            if left == right == None:
                return True
            if left and right:
                if left.val == right.val:
                    left_ans = is_sym(left.right, right.left)
                    right_ans = is_sym(left.left, right.right)
                    return left_ans and right_ans
                else:
                    return False
            return False
        return is_sym(root.left, root.right)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 试一试层序遍历
        def is_sym(l):
            if len(l) & 1:
                return False
            else:
                mid = len(l) >> 1
                if l[:mid] == l[mid:][::-1]:
                    return True
                return False

        if root == None:
            return True
        judge = [root.val]
        node_s = [root]
        while node_s:
            new_s = []
            judge = []
            for node in node_s:
                if node.left:
                    new_s.append(node.left)
                    judge.append(node.left.val)
                else:
                    judge.append(None)
                if node.right:
                    new_s.append(node.right)
                    judge.append(node.right.val)
                else:
                    judge.append(None)
            if len(judge) and not is_sym(judge):
                return False
            node_s = new_s
        return True

test = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(test.isSymmetric(root))