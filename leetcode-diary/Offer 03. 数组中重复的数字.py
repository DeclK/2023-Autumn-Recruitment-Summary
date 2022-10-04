import collections
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for key in counter:
            if counter[key] > 1:
                return key
        return None