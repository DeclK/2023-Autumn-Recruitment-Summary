from turtle import right
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 二分查找
        for idx, i in enumerate(nums):
            if i >= target: break
            res = target - i
            from bisect import bisect_left
            index = bisect_left(nums, res, lo=idx)
            if index < len(nums) and nums[index] == res:
                return [i, res]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表
        s = set(nums)
        for i in nums:
            if i >= target: break
            res = target - i
            if res in s:
                return [i, res]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 双指针
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [nums[left], nums[right]]

test = Solution()
nums = [14,15,16,22,53,60]
target = 76
print(test.twoSum(nums, target))