from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            mask = 1 << i
            num0, num1 = 0, 0
            for i in nums:
                if i & mask: num1 += 1
                else: num0 += 1
            if num0 % 3 == 0: ans = ans | mask
        return ans

test = Solution()
nums = [1, 1, 2, 1]
print(test.singleNumber(nums))