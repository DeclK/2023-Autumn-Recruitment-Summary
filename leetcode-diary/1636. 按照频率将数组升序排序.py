from typing import List

import collections
import functools


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)

        def compare(x, y):
            if x[1] > y[1]: return 1
            if x[1] < y[1]: return -1
            if x[1] == y[1] and x[0] > y[0]: return -1
            if x[1] == y[1] and x[0] < y[0]: return 1
            else: return 0
        l = list(counter.items())
        print(l)
        l = sorted(l, key=functools.cmp_to_key(compare))
        ret = []
        for key, val in l:
            ret += [key] * val
        return ret

test = Solution()
nums = [2,2,2,1,3]
print(test.frequencySort(nums))