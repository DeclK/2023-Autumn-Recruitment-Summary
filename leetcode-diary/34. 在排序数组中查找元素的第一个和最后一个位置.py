from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        if len(nums) == 0: return -1, -1
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or target != nums[left]:
            return -1, -1
        right = bisect.bisect_right(nums, target)
        return left, right - 1

nums = [0]; target = 0
test = Solution()
print(test.searchRange(nums, target))