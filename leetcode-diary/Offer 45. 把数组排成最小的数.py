import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y < y + x: return 0
            elif x + y > y + x: return 1
            else: return 0
        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(compare))
        return ''.join(nums)

test = Solution()
nums = [123,321]
print(test.minNumber(nums))