# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # 遍历 + 递归
        def check(node, root):
            # 从某个 Node 开始是否符合
            if node and root:
                if node.val == root.val:
                    return check(node.left, root.left) and check(node.right, root.right)
            elif node is None and root is None:
                return True
            return False
        def travers(root):
            nonlocal ans
            if not root: return
            if ans == True: return
            ans = check(root, subRoot)
            travers(root.left)
            travers(root.right)
        ans = None
        travers(root)
        return ans