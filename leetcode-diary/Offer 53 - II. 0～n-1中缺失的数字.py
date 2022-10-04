from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid < nums[mid]:
                right = mid - 1
            elif mid == nums[mid]:
                left = mid + 1
        return left

test = Solution()
nums = [0,1,2,3,4,5,6,7]
print(test.missingNumber(nums))