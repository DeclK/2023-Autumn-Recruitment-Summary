from sys import flags
from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 这种想法超出了限制，因为最终的答案数将很大，循环将无法完成
        def numdistinct(s, t) -> List:
            ret = []
            if len(t) == 1:
                for idx, s_ in enumerate(s):
                    if s_ == t:
                        ret.append(idx)
                return ret
            sub_list = numdistinct(s, t[:-1])
            last = t[-1]
            for idx in sub_list:
                if idx + 1 < len(s):
                    for idx_, s_ in enumerate(s[idx + 1:]):
                        if s_ == last:
                            ret.append(idx_ + idx + 1)
            return ret
        l = numdistinct(s, t)
        return len(l)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 新想法使用动态规划，着力点依然在如何增加组合数上
        # 如果 s 新增了一个字母 x，如果 x 是 t 的最后一个字母，那么最终答案为 s 中原本的组合数加上 s 中 t[:-1] 的组合数
        # 显然我们的状态就出来了，就是 s 中每个长度 t[:(1~n)] 的组合数
        # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] if s[i] == t[j] (and i <= j
        m, n = len(s), len(t)
        dp = [[0] * (1 + n) for i in range(1 + m)]
        for i in range(1 + m):
            # 表格中的最左侧一列，这样就不用考虑边界条件了
            dp[i][0] = 1
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # 新增的 + 本身就有的
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]
                

test = Solution()
s = 'babgbag'
t = 'bag'
s = "aacaacca"
t = "ca"
s = 'bbb'
t = 'bb'
# s = "adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
# t = "bcddceeeebecbc"
print(test.numDistinct(s, t))