import collections
from itertools import accumulate
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 先看复杂度排除动态规划, 然而滑动窗口并不好维护窗口中的性质,
        # 所以进一步考虑该题的本质, 既然是要被 k 整除, 那么其前缀和对 k 的余数一定相等
        prefix_sum = list(accumulate(nums))
        mark = [i % k for i in prefix_sum]
        counter = collections.Counter(mark)
        ans = 0
        for key, val in counter.items():
            if key == 0:
               ans += val * (val + 1) / 2 
            else:
                ans += val * (val - 1) / 2
        return int(ans)


test = Solution()
nums = [4,5,0,-2,-3,1]
k = 13
print(test.subarraysDivByK(nums, k))