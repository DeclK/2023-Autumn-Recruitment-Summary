import bisect
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        srt = sorted(nums)
        l = []
        n = len(nums)
        ret = []
        # 记录已经计算的数字
        for i in range(n - 1, -1, -1):
            index = bisect.bisect_left(l, nums[i])
            # 在已经计算的数字中，哪些比当前数字要小的，会被重复计算，需要删除
            l.insert(index, nums[i])
            ret.append(index)
        return ret[::-1]

# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         # 使用二分查找位置，并让其 remove
#         # 这种写法会超时
#         srt = sorted(nums)
#         ret = []
#         for i in nums:
#             index = bisect.bisect_left(srt, i)
#             ret.append(index)
#             srt.pop(index)
#         return ret

nums = [5,2,6,1]
test = Solution()
print(test.countSmaller(nums))