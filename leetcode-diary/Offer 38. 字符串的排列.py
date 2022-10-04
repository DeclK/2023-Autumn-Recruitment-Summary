import itertools
from turtle import st
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = []
        def dfs(path, string):
            if len(string) == 0:
                ans.append(path)
                return
            tempt = {}
            for idx, s_ in enumerate(string):
                if s_ not in tempt:
                    new_s = string[:idx] + string[idx+1:]
                    tempt[s_] = 1
                    dfs(path + s_, new_s)
        dfs('', s)
        return ans

test = Solution()
s = 'aab'
print(test.permutation(s))

