from typing import List

from torch import nuclear_norm


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先对 k 取余数
        n = len(nums)
        k = k % n
        nums[:] = nums[::-1]
        nums[k:] = nums[k::][::-1]
        nums[:k] = nums[:k][::-1]
        print(nums)

test = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(test.rotate(nums, 3))