from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return end
        while begin <= end:
            mid = (end + begin) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return begin

nums = [1,3,5,6]
test = Solution()
print(test.searchInsert(nums, 2))