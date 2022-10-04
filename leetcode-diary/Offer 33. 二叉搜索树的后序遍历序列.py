from inspect import stack
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 遍历进行判断
        if len(postorder) == 0:
            return True
        root = postorder[-1]
        def jugde(l, num):
            return all([i > num for i in l])
        left = []
        for idx, i in enumerate(postorder[:-1]):
            if i < root:
                left.append(i)
            else:break
        right = postorder[len(left):-1]
        if jugde(right, root):
            left_ans = self.verifyPostorder(left)
            right_ans = self.verifyPostorder(right)
            return left_ans & right_ans
        else:
            return False

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 使用单调栈解决，时间复杂度 O(n)
        if len(postorder) == 0:
            return True
        stack = []
        root = 1e9
        postorder = postorder[::-1]
        stack.append(postorder[0])
        for i in postorder:
            if i > root: return False
            while stack and i < stack[-1]:
                root = stack.pop()
            stack.append(i)
        return True                    

test = Solution()
order = [1,2,5,10,6,9,4,3]
print(test.verifyPostorder(order))