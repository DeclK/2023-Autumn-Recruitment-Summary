class Solution:
    def countSubstrings(self, s: str) -> int:
        # 做两个 n**2
        # 首先肯定要指导某个子串是不是回文，这就引出了状态 dp[i][j] 对应是否为回文
        # 获得过后就将其计算入子串数量
        n = len(s)
        dp = [[0] * n for i in range(n)]  
        # dp[i][j] = True if dp[i - 1][j - 1] = True and s[i] == s[j]
        ans = 0
        for j in range(n):
            dp[j][j] = 1
            ans += 1
            for i in range(j - 1, -1, -1):
                if (dp[i + 1][j - 1] == 1 or i == j -1) and s[i] == s[j]:
                    dp[i][j] = 1
                    ans += 1
        return ans

test = Solution()
s = 'aaa'
print(test.countSubstrings(s))