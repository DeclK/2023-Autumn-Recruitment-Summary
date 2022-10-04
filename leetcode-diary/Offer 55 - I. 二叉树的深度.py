# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 直接遍历就完事儿了
        depth = 0
        def travers(root, dep):
            nonlocal depth
            if root == None: return
            if root.left == root.right == None:
                depth = max(depth, dep)
            travers(root.left, dep + 1)
            travers(root.right, dep + 1)
        travers(root, 1)
        return depth

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def traverse(root, depth):
            if root == None: return depth - 1
            left = traverse(root.left, depth + 1)
            right = traverse(root.right, depth + 1)
            return max(left, right)
        return traverse(root, 1)

test = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(test.maxDepth(root))