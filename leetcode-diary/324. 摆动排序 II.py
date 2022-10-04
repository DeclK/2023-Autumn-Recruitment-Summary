from tkinter import SOLID
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 最直接的想法, 进行排序, 一个最小, 一个最大的进行排序
        sort_nums = sorted(nums)
        n = len(nums)
        left = sort_nums[:(n + 1) // 2]
        p_left = len(left) - 1
        right = sort_nums[(n + 1) // 2:]
        p_right = len(right) - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left[p_left]
                p_left -= 1
            else:
                nums[i] = right[p_right]
                p_right -= 1
        print(nums)

test = Solution()
nums = [1,3, 3, 10]
print(test.wiggleSort(nums))