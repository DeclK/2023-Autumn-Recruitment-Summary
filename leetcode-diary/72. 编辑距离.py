class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        # dp[n][m] denote the minimum distance of n & m 
        # initial
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cur_i = i - 1
                cur_j = j - 1
                if word1[cur_i] == word2[cur_j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[n][m]

test = Solution()
word1 = "horse"; word2 = "ros"
print(test.minDistance(word1, word2))