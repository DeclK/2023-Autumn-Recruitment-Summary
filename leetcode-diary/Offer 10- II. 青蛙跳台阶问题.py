class Solution:
    def numWays(self, n: int) -> int:
        # 搜索算法超时了，改为动态规划
        if n == 0:
            return 0
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
