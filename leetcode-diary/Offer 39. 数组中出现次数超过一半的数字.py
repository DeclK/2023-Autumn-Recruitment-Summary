from inspect import _void
import numbers
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        ans = 0
        for i in nums:
            if vote == 0:
                ans = i
                vote += 1
            else:
                if i == ans:
                    vote += 1
                else:
                    vote -= 1
        return ans

test = Solution()
nums = [1, 1, 2, 3, 1]
print(test.majorityElement(nums))
            