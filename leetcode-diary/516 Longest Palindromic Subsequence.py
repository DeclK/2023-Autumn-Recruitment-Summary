class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        # 不能用 [[0] * n] * n 因为这样列表中的成员指向的是同一个

        # 注意遍历顺序，需要从短到长的遍历，并且有一个倒序
        for j in range(0, n):
            dp[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

test = Solution()
s = 'bbbab'
print(test.longestPalindromeSubseq(s))