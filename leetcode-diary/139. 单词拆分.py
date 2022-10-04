from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        def check(s):
            """ check current string will match wordDict """
            ret = False
            for word in wordDict:
                m = len(word)
                k = len(s)
                if k < m:
                    ret |= False
                else:
                    ret |= s[-m:] == word and dp[k - m]
            return ret

        for i in range(1, n + 1):
            dp[i] = check(s[:i])
        return dp[n]

test = Solution()
s = "applepenapple"; wordDict = ["apple", "pen"]
print(test.wordBreak(s, wordDict))