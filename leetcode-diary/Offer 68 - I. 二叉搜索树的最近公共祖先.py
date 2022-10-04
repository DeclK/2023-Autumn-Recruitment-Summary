# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 先进行搜索，然后存入路径
        two_path = []
        path = []
        def dfs(node):
            nonlocal path
            if node == None: return
            if node.val == p.val:
                two_path.append(path + [node])
            if node.val == q.val:
                two_path.append(path + [node])
            path.append(node)
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        path1 = two_path[0]
        path2 = two_path[1]
        for i in path1[::-1]:
            if i in path2:
                return i

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # 没有利用二叉搜索树的性质
#         # 如果目标一个比根节点小，一个比根节点大，该节点就是共同祖先，否则可以选择左右子树进行搜索
#         v1 = min(q.val, p.val)
#         v2 = max(q.val, p.val)
#         ans = None
#         def dfs(node):
#             nonlocal ans
#             if node == None: return 
#             if v2 > node.val > v1:
#                 ans = node
#                 return
#             elif node.val > v2:
#                 dfs(node.left)
#             else: dfs(node.right)
#         dfs(root)
#         return ans

test = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(6, TreeNode(7), TreeNode(9)))
p = TreeNode(7)
q = TreeNode(9)
print(test.lowestCommonAncestor(root, p, q))