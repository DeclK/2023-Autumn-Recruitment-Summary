from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # bisect
        n = len(nums) - 1
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            left_count = 0
            for i in range(n + 1):
                if nums[i] <= mid:
                    left_count += 1
            if left_count > mid:
                right = mid
            else:
                left = mid + 1
        return left

test = Solution()
nums = [1,3,2,4,3]
print(test.findDuplicate(nums))