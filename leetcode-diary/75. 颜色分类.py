from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 times will solve it
        index = 0
        n = len(nums)
        for j in range(2):
            for i in range(n):
                if nums[i] == j:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
        
test = Solution()
nums =[2, 1, 0]
test.sortColors(nums)
print(nums)