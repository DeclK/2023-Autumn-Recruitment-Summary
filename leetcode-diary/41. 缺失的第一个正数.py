from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums[:] = [i if i > 0 else 1000000 for i in nums]
        n = len(nums)
        for i in nums:
            # 提取原始信息
            i = abs(i)
            res = (i - 1) % n 
            check = (i - 1) // n
            if check == 0 and nums[res] > 0:
                nums[res] *= -1 
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

test = Solution()
nums = [3,4,-1,1]
print(test.firstMissingPositive(nums))