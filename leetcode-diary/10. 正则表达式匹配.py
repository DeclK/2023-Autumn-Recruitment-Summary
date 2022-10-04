class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        def match(index_j, index_i):
            if p[index_j] == s[index_i]: return True
            if p[index_j] == '.': return True

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[0][0] = True
                    continue
                index_i = i - 1
                index_j = j - 1
                if index_j > 0 and p[index_j] == '*':
                    if match(index_j - 1, index_i):
                        dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    if match(index_j, index_i):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        print(dp)
        return dp[n][m]


s = 'a'
p = '.*'
test = Solution()
print(test.isMatch(s, p))

