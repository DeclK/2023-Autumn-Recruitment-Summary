# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 解决方法就是对每一个根节点重复计算, 这样是 N 方复杂度
        # 现在使用前缀和进行解决
        ans = 0
        from collections import defaultdict
        presum_set = defaultdict(int)
        presum_set[0] = 1
        def dfs(node, presum_set, presum):
            nonlocal ans
            if not node: return
            presum += node.val
            target = presum - targetSum
            if presum_set[target] >= 1:
                ans += presum_set[target]
            presum_set[presum] += 1
            dfs(node.left, presum_set, presum)
            dfs(node.right, presum_set, presum)
            presum_set[presum] -= 1
        dfs(root, presum_set, 0)
        return ans

test = Solution()
root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
# root = TreeNode(1)
targetsum = 18
# targetsum = 0
print(test.pathSum(root, targetsum))

