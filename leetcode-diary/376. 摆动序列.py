from tabnanny import check
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 动态规划, 记录以 i 节为的 wiggle 最长子序列, i 要有两种状态
        # i 为高 0, i 为低 1
        n = len(nums)
        dp = [[1, 1] for i in range(n)]
        # dp[0] = [1, 1]
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                    ans = max(ans, dp[i][0])
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                    ans = max(ans, dp[i][1])
        return ans

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 去除连续单调的数字
        n = len(nums)
        if n < 2: return n
        stack = nums[:2]
        def check_mono(a, b):
            if a > b: return 'de'
            if a < b: return 'in'
            if a == b: return 'eq'
        for i in range(2, n):
            status_1 = check_mono(stack[-2], stack[-1])
            status_2 = check_mono(stack[-1], nums[i])
            if status_1 == 'de' and status_2 == 'in':
                stack.append(nums[i])
            elif status_1 == 'in' and status_2 == 'de':
                stack.append(nums[i])
            else:
                stack.pop()
                stack.append(nums[i])
        if len(stack) == 2 and check_mono(stack[-2], stack[-1]) == 'eq':
            return 1
        return len(stack)


test = Solution()
nums = [1,1]
print(test.wiggleMaxLength(nums))