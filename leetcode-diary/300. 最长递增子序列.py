from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in nums]
        ret = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ret = max(dp[i], ret)
            
        return ret
test = Solution()
nums = [0,0,1]
print(test.lengthOfLIS(nums))