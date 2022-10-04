class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        def update(i, j):
            if i == j == 0:
                dp[i][j] = 1
                return
            a = dp[i - 1][j] if i - 1 >= 0 else 0
            b = dp[i][j - 1] if j - 1 >= 0 else 0
            dp[i][j] = a + b
        for i in range(m + n):
            cur_i = max(0, i - n + 1)
            cur_j = min(n - 1, i)
            while cur_i <= m - 1 and cur_j >= 0:
                update(cur_i, cur_j)
                cur_i += 1
                cur_j -= 1
        return dp[m - 1][n - 1]
                

test = Solution()
print(test.uniquePaths(3, 7))