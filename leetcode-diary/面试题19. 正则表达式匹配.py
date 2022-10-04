from tkinter.tix import Tree


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 状态方程很难写出来，只勉强写了一些为 true 的，想不到就通过了！！
        # dp[i][j] = true if dp[i - 1][j - 1] and s[j] == p[i] (* or not both can
        # dp[i][j] = true if dp[i - 1][j] and p[i] == *
        # dp[i][j] = true if dp[i][j - 1] and s[j] == p[i] == *
        s = list(s)
        pa = []
        for idx, i in enumerate(p):
            if idx != len(p) - 1 and p[idx + 1] == '*':
                pa.append(i + '*')
            elif i != '*': pa.append(i)
        # print(pa)
        n = len(pa)
        m = len(s)
        dp = [[False] * (m + 1) for k in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                # 由于需要判断空，所以要从零开始判断
                sj = s[j - 1] if j > 0 else ''
                pi = pa[i - 1]
                if '*' in pi:
                    if (pi[0] == sj or pi[0] == '.') and dp[i][j - 1]: 
                        dp[i][j] = True
                    if (pi[0] == sj or pi[0] == '.') and dp[i - 1][j - 1]: 
                        dp[i][j] = True
                    if dp[i - 1][j]: 
                        dp[i][j] = True
                else:
                    if sj != '' and (pi == '.' or pi == sj) and dp[i - 1][j - 1]: 
                        dp[i][j] = True
        return dp[n][m]

test = Solution()
s = "mississippi"
p = "mis*is*p*."
# s = "aab"
# p = "c*a*b"
s = "a"
p = ".*..a*"
print(test.isMatch(s, p))
