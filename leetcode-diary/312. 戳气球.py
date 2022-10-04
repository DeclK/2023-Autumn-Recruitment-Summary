from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # open area, last one to kick
        n = len(nums)

        # padding 2
        nums.append(1)
        nums.insert(0, 1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for j in range(n + 2):
            for i in range(j, -1, -1):
                if i >= j - 1:
                    dp[i][j] = 0
                else:
                    for k in range(i + 1, j):
                        dp[i][j] = max(dp[i][j], nums[i] * nums[j] * nums[k] + dp[i][k] + dp[k][j])

        return dp[0][n + 1]

test = Solution()
nums = [3,1,5,8]
print(test.maxCoins(nums))