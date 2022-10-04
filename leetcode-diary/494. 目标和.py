from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * 4001 for _ in range(n + 1)]
        # dp[i][j] use i numbers, sum is j
        origin = -2000
        dp[0][0-origin] = 1
        for i in range(1, n + 1):
            index_i = i - 1
            for j in range(-2000, 2001):
                cur_pos = j - origin
                if cur_pos - nums[index_i] >= 0:
                    dp[i][cur_pos] += dp[i - 1][cur_pos - nums[index_i]]
                if cur_pos + nums[index_i] <= 4000:
                    dp[i][cur_pos] += dp[i - 1][cur_pos + nums[index_i]]
        return dp[n][target - origin]
        
        # dfs solution
        n = len(nums)
        self.ans = 0
        def dfs(idx, ans):
            if ans > target + 100 or ans < target - 1000:
                return
            if idx == n:
                if target == 0:
                    self.ans += 1
                return 
            dfs(idx + 1, ans + nums[idx])
            dfs(idx + 1, ans - nums[idx])
        dfs(0, target)
        return self.ans

test = Solution()
nums = [1,1,1]; target = 3
print(test.findTargetSumWays(nums, target))