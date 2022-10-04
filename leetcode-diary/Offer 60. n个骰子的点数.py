from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # 6^11 次方还是挺大的，所以放弃搜索，必须尝试动态规划
        # 添加骰子才会让事情变得更加简单 dp[i][j] 代表骰子个数 i 和为 j
        # dp[i][j] = dp[i - 1][j - 1] +...+ dp[i - 1][j - 6]
        low = n
        high = 6 * n
        dp = [[0] * (high + 1) for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, high + 1):
                for k in range(1, 7):
                    dp[i][j] += dp[i - 1][j - k]
        summ = sum(dp[n])
        return [count / summ for count in dp[n][n:]]
        
        
        
        
        
        
        
        ans = [0 for i in range(low, high + 1)]
        def dfs(pos, val):
            if pos == n:
                ans[val - low] += 1
                return
            for i in range(1, 7):
                dfs(pos + 1, val + i)
        dfs(0, 0)
        return ans 

test = Solution()
n = 11
print(test.dicesProbability(n))


