from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        def legal(num): return 0 <= num < len(nums)
        while left <= right:
            mid = (left + right) // 2
            if legal(mid + 1) and legal(mid - 1):
                if nums[mid + 1] > nums[mid]: left = mid + 1
                elif nums[mid - 1] > nums[mid]: right = mid - 1
                else: 
                    return mid
            elif legal(mid + 1):
                if nums[mid] > nums[mid + 1]: return mid
                else: left = mid + 1
            elif legal(mid - 1): return mid
            else: return mid


test = Solution()
nums = [1, 2]
print(test.findPeakElement(nums))
