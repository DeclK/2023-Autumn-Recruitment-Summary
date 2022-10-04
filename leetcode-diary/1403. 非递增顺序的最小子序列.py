from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        accum = sum(nums)
        ret = []
        summ = 0
        while summ <= accum:
            cur = nums.pop(0)
            ret.append(cur)
            summ += cur
            accum -= cur
        return ret

test = Solution()
nums = [4,3,10,9,8]
print(test.minSubsequence(nums))