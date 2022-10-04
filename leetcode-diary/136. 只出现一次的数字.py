from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = None
        for num in nums:
            if ret is None:
                ret = num
                continue
            ret = ret ^ num
        return ret