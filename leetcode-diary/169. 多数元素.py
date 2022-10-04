from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        ret = nums[0]
        for num in nums:
            if vote == 0:
                ret = num 
            if num == ret:
                vote += 1
            else:
                vote -= 1

        return ret