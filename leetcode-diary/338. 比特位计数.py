from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j = i & (i - 1)
            dp[i] = dp[j] + 1
        return dp

test = Solution()
print(test.countBits(5))