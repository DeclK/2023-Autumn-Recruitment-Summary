class Solution:
    def numSquares(self, n: int) -> int:
        s_list = [num ** 2 for num in range(1, 101)]
        dp = [1e5] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for squre in s_list:
                if squre > i: break
                dp[i] = min(dp[i - squre] + 1, dp[i])
        return dp[n]

test = Solution()
n = 4
print(test.numSquares(n))
