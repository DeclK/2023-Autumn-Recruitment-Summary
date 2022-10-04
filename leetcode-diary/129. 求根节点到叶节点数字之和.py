# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # dfs + a list to store path
        self.ans = 0

        def get_sum(path):
            ans = 0
            if len(path) > 0:
                for num in path:
                   ans = ans * 10 + num 
            return ans

        def dfs(node, path):
            if node is None: return
            if node.left is None and node.right is None:
                path = path + [node.val]
                self.ans += get_sum(path)
                return
            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])
            
        dfs(root, [])
        return self.ans


node = TreeNode(1, TreeNode(2), TreeNode(3))

test = Solution()
ans = test.sumNumbers(node)
print(ans)
