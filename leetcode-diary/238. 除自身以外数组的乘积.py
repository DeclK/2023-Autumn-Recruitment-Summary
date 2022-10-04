from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 剑指 offer 原题, 使用上下三角
        n = len(nums)
        upper = [1] * n
        down = [1] * n
        for i in range(1, n):
            down[i] = down[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            upper[i] = upper[i + 1] * nums[i + 1]
        ans = [1] * n
        for i in range(n):
            ans[i] = upper[i] * down[i]
        return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 尝试常数空间
        n = len(nums)
        ans = [1] * n
        upper = 1
        down = 1
        for i in range(n - 1):
            upper *= nums[i]
            ans[i + 1] *= upper
        for i in range(n - 1, 0, -1):
            down *= nums[i]
            ans[i - 1] *= down
        return ans