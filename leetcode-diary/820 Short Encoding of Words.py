from sys import flags
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 既然已经完全摒弃了顺序思路，那不如逐个攻破
        # 只有两个字符串完全相同，或者一个字符串是另一个字符串的后缀，这样才能合并
        # 由此思路解题
        d = dict.fromkeys(words, 0)
        ans = []
        def absorb(s):
            if d[s] == 0:
                for i in range(len(s) - 1):
                    post = s[i + 1:]
                    if d.get(post) == 0:
                        d[post] = 1
                ans.append(s)
                d[s] = 1
        words = sorted(words, key=lambda x: len(x), reverse=True)
        for i in words:
            absorb(i)
        ans = '#'.join(ans) + '#'
        return len(ans)






test = Solution()
words = ["time", "me", "bell"]
# words = ["time","atime","btime"]
print(test.minimumLengthEncoding(words))
