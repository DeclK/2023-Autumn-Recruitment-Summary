from re import L
from turtle import right
from typing import List
from importlib_metadata import functools

from pyparsing import nums


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 一开始选择了固定 k, 使用一个滑窗思想, 其实这样并不方便
        # 即使有了滑窗也不太好判断数字是否落在了区间内
        nums = [(value, idx) for idx, value in enumerate(nums)]
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 1):
            left = i
            right = i + 1
            while right < n and abs(nums[left][0] - nums[right][0]) <= t:
                if abs(nums[left][1] - nums[right][1]) <= k:
                    return True
                right += 1
        return False


test = Solution()
nums = [1,5,9,1,5,9]
k = 3
t = 2
# nums = [1,2,3,1]
# k = 3
# t = 0
print(test.containsNearbyAlmostDuplicate(nums, k, t))