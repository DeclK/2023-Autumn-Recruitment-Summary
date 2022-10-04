import collections
import random
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 使用一个指针维护最近的有空缺的数字
        s = set(nums)
        s_nums = sorted(s)
        m = len(s_nums)
        counter = collections.Counter(nums)
        empty = s_nums[0]
        ret = 0
        for i in range(m):
            if counter[s_nums[i]] == 1:
                continue
            val = counter[s_nums[i]]
            for _ in range(val - 1):
                # 寻找空隙
                while empty <= s_nums[i] or empty in s:
                    empty += 1
                ret += empty - s_nums[i]
                # s.add(empty)
                # 当前空隙被占领, 跳过去
                empty += 1
        return ret


test = Solution()
nums = [random.randint(0, 7) for _ in range(5)]
print(sorted(nums))
nums = [4, 4, 5, 5, 5]
print(test.minIncrementForUnique(nums))
