from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 以 i 结尾的最大连续子数组和
        # dp[i + 1] = dp[i] or dp[i] + nums[i]
        n = len(nums)
        if n == 0:
            return None
        dp = [0] * n
        dp[0] = nums[0]
        ret = -1e5
        for i in range(1, n):
            if nums[i] <= 0:
                dp[i] = max(nums[i], nums[i] + dp[i])
            else:
                dp[i] = dp[i - 1] + nums[i]
            ret = max(ret, dp[i])
        return ret