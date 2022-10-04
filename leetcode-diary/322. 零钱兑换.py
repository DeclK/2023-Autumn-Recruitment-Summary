from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e5] * (amount + 1)
        dp[0] = 0
        n = len(coins)
        for j in range(1, amount + 1):
            for i in range(n):
                if j - coins[i] >= 0:
                    dp[j] = min(dp[j - coins[i]] + 1, dp[j])
        return dp[amount] if dp[amount] < 1e5 else -1


test = Solution()
coins = [1, 2, 5]; amount = 0
print(test.coinChange(coins, amount))

