import bisect
from itertools import accumulate
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 先考虑了一下动态规划, 但发现要平方复杂度
        # 马上考虑了双指针, 定义指针所指的和为考虑指标
        left = 0
        right = -1
        n = len(nums)
        summ = 0
        ans = 0
        while right < n - 1:
            right += 1
            summ += nums[right]
            # 要清晰定义循环的开始与结束状态
            while summ >= target:
                ans = min(ans, right - left + 1) if ans else right - left + 1
                summ -= nums[left]
                left += 1
        # print(left, right)
        return ans

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         # 尝试用二分查找优化原始平方复杂度
#         # 前缀和是一个有序的序列可以方便进行二分
#         # presum[k] 代表 0 ~ k - 1 个数字的和, prefix[n - 1] 代表所有数字的和
#         presum = list(accumulate(nums))
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             # 以 index i 作为起始点进行搜索
#             pre = presum[i] - nums[i]# 到这个数之前的和
#             t = pre + target
#             index = bisect.bisect_left(presum, t)
#             if index < n:
#                 ans = min(index - i + 1, ans) if ans else index - i + 1
#         return ans
        

test = Solution()
target = 4
nums = [1,4,4]
# nums = [2,3,1,2,4,3]
# nums = [1,1,1,1,1,1,1,1]
print(test.minSubArrayLen(target, nums))