from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[zero_index] = \
                nums[zero_index], nums[i]
                zero_index += 1
        return nums

nums = [0,1,2,1,2]
test = Solution()
print(test.moveZeroes(nums))