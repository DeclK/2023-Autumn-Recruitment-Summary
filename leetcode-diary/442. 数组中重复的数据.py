from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        x = 0
        for i in nums:
            if (x >> i) & 1: res.append(i)
            else: x |= 1 << i
        return res