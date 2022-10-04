# Definition for a binary tree node.
from os import path
from turtle import right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 深度搜索
        paths = []
        def dfs(node, path: list):
            if not node: return
            path.append(node)
            if node.val == p.val:
                paths.append(path[:])
            if node.val == q.val:
                paths.append(path[:])
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        path1 = paths[0]
        path2 = paths[1]
        index = -1
        n = len(path1)
        m = len(path2)
        for i in range(n):
            if i < m - 1 and path1[i].val != path2[i].val:
                index = i - 1
        return path1[index]

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return
        if root == q or root == p: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root