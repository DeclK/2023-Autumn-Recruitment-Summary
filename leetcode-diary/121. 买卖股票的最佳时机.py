from turtle import left
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只需要知道其右侧的最大数值即可
        n = len(prices)
        store = [1e5] * n
        maxi = -1
        for i in range(n - 1, 0, -1):
            if prices[i] > maxi:
                maxi = prices[i]
            store[i - 1] = maxi
        ans = 0 
        for i in range(n - 1):
            ans = max(ans, store[i] - prices[i])
        return ans
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这是第二版
        # 只需要知道底部和顶部在哪里即可
        n = len(prices)
        if n <= 1: return 0
        stack = [0] * n
        for i in range(n):
            if i == 0:
                if prices[i + 1] > prices[i]: stack[i] = -1
                elif prices[i + 1] < prices[i]: stack[i] = 1
                else: stack[i] = 0
            elif i < n - 1:
                if prices[i + 1] <= prices[i] > prices[i - 1] or prices[i + 1] < prices[i] >= prices[i - 1]: stack[i] = 1
                elif prices[i - 1] >= prices[i] < prices[i + 1] or prices[i - 1] > prices[i] <= prices[i + 1]: stack[i] = -1
            elif i == n - 1:
                if prices[i] > prices[i - 1]: stack[i] = 1
                elif prices[i] < prices[i - 1]: stack[i] = -1
                else: stack[i] = 0
        buy = None
        ans = 0
        for i in range(n):
            if stack[i] == -1:
                buy = prices[i]
            if stack[i] == 1:
                ans += prices[i] - buy if buy != None else 0
                buy = None
        return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 写一下第二题的最优版本
        n = len(prices)
        if n <= 1: return 0
        dp1 = 0   # 持有1个股票的最大利润
        dp2 = 0   # 不持有股票的最大利润
        for i in range(n):
            if i == 0:
                dp1 = -prices[i]
                continue
            dp1 = max(dp1, dp2 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
        return dp2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这是第三题, 和我之前在美团面的一道题很想
        # 打算用两次动态规划解决
        # dp[j] 定义为第 j 天最小的值 left => right
        # dp[i] 定义为第 i ~ n 中最大的值 right => left
        n = len(prices)
        mini = 0
        dp_a = [0] * n
        maxi = 0
        dp_b = [0] * n
        for i in range(n):
            if i == 0: 
                mini = prices[i]
                dp_a[i] = 0
            else:
                mini = min(mini, prices[i])
                profit = prices[i] - mini
                dp_a[i] = max(dp_a[i - 1], profit)

        for i in range(n - 1, -1, -1):
            if i == n - 1: 
                maxi = prices[i]
                dp_b[i] = 0
            else:
                maxi = max(maxi, prices[i])
                profit = maxi - prices[i]
                dp_b[i] = max(dp_b[i + 1], profit)

        ans = 0
        for i in range(n):
            profit = dp_a[i] + dp_b[i]
            ans = max(ans, profit)
        return ans

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 这是买卖股票终极版本, 可以交易 k 次
        # dp[i][2k] 代表第 i 天最多交易 k 次的状态
        # dp[i][2k] = max(dp[i - 1][2k], dp[i - 1][2k - 1] + prices[i])
        # dp[i][2k + 1] = max(dp[i - 1][2k + 1], dp[i - 1][2k] - prices[i])
        n = len(prices)
        if n == 0: return 0
        dp = [0] * (2 * k + 1)
        # 更新第一天的所有状态
        for i in range(2 * k + 1):
            if i % 2 == 1:
                dp[i] = -prices[0]
        for i in range(n):
            for j in range(1, 2 * k + 1):
                if j % 2 == 0:
                    # 双数
                    # 是否卖出
                    dp[j] = max(dp[j], dp[j - 1] + prices[i])
                else:
                    # 单数
                    # 是否买入
                    dp[j] = max(dp[j], dp[j - 1] - prices[i])
        return dp[-1]
        

test = Solution()
prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [1]
k = 3
print(test.maxProfit(k, prices))