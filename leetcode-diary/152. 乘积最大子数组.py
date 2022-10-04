from random import randint
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 明显的动态规划问题
        # dp[i] = max(dp[i - 1] * nums[i], nums[i])
        # 需要知道以前一个数正数的最大值与负数的最小值
        # dp[i] = if nums[i] < 0 dp[i] = mini * nums[i]
        n = len(nums)
        if n == 1: return nums[0]
        mini = 0
        maxi = 0
        # 只用了前一个, 所以可以进行优化
        ans = 0
        for i in range(n):
            if i == 0:
                maxi = max(0, nums[i])
                mini = min(0, nums[i])
                ans = maxi
                continue
            if nums[i] < 0:
                mini_ = mini
                mini = min(maxi * nums[i], nums[i])
                maxi = max(mini_ * nums[i], 0)
                ans = max(maxi, ans)
            else:
                mini = min(mini * nums[i], 0)
                maxi = max(maxi * nums[i], nums[i])
                ans = max(maxi, ans)
        return ans

test = Solution()
nums = [4, -1, 0, -2, 1, -3]
print(test.maxProduct(nums))