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

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # recursive method, can't solve large cases
        n = len(word1)
        m = len(word2)
        if n == 0: return m
        if m == 0: return n
        a = word1[-1]
        b = word2[-1]
        if a == b:
            return self.minDistance(word1[:-1], word2[:-1])
        mini1 = self.minDistance(word1[:-1], word2)
        mini2 = self.minDistance(word1, word2[:-1])
        mini3 = self.minDistance(word1[:-1], word2[:-1])
        mini = min(mini1, mini2, mini3)
        return mini + 1

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                    continue
                index_i = i - 1
                index_j = j - 1
                si = word1[index_i]
                sj = word2[index_j]
                if si == sj:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[n][m]

test = Solution()
word1 = "intention";  word2 = "execution"
# word1 = "i";  word2 = "exe"
print(test.minDistance(word1, word2))