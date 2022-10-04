from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        num = 0
        n = len(coins)
        def search(pos, target):
            nonlocal num
            if target == 0:
                num += 1
                return
            if pos == n or coins[pos] > target:
                return
            for i in range(pos, n):
                # 进入子搜索空间
                times = target // coins[i]
                for r_ in range(1, times + 1):
                    search(i + 1, target - r_ * coins[i])
        search(0, amount)
        return num
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #       amount 1 2 3 4 5
        # coin1        1 1 1 1 1
        # coin2        1 2 2 3 3
        # coin5        1 2 2 3 4
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-coins[i]]
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

test = Solution()
amount = 11
coins = [3,5,7,8,9,10]
print(test.change(amount, coins))
4227159
9303078
35502874