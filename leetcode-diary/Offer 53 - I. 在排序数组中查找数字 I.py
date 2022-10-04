from tkinter import FLAT
from typing import List
import collections
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        counter = collections.Counter(nums)
        return counter[target] if counter.get(target) else 0

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return right - left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 再写一遍二分查找
        # 这是使用 Left 寻找右侧值
        def bisect_right(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        left = bisect_right(nums, target) 
        right = bisect_right(nums, target - 1)
        return left - right


test = Solution()
nums = [5,7,7,8,8,10]
# nums = [1]
nums = [1, 3]
nums = [2, 2]
target = 1
print(test.search(nums, target))