from turtle import left, right
from typing import List

from pyparsing import nums
from pyrsistent import CheckedKeyTypeError


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 使用动态规划 这题的状态转移仍然需要两个维度
        # dp[i][j] = min{max(dp[i - k][j - 1], sum(i-k+1:i+1))}
        # 这一题教会了我如何进行初始化，只需要关注有减号的地方，当这些地方超过了数组的范围，就需要进行初始化，然后更改循环范围即可
        n = len(nums)
        dp = [[10000] * (m + 1) for i in range(n)]
        for i in range(n):
            # index i
            for j in range(1, m + 1):
                if j == 1:
                    dp[i][j] = sum(nums[:i + 1])
                    continue
                for k in range(j - 2, i):
                    # 从第 j - 1 个数字到第 i 个数字, 重复 i - j + 2次
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum(nums[k + 1:i + 1])))
        print(dp)
        return dp[n - 1][m]

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 本题的最佳解法, 二分查找 + 贪心算法
        # 单个最大值~和之间, 假设一个值 x, 判断整个数组能不能分成 m 份, 每一份都小于 x
        # 通过二分查找，很快就能找到这个值
        def check(x):
            count = 1
            tempt = 0
            for i in nums:
                tempt += i
                if tempt > x:
                    tempt = i
                    count += 1
            if count <= m: return True
                # 能够分成 m 份, 每一份都小于等于 x
            else: return False
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            result = check(mid)
            if result == True:
                right = mid - 1
            else:
                left = mid + 1
        return left


test = Solution()
nums = [1, 2, 3, 4, 5]
nums = [7, 2, 5, 10, 8]
nums = [1, 4, 4]
print(test.splitArray(nums, 2))