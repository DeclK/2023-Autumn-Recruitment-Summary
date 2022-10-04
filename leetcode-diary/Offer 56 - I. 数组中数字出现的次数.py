import heapq
from typing import List
import collections

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 使用位运算
        c = 0
        for i in nums:
            c = c ^ i
        mask = 0
        for i in range(32):
            mask = 1 << i
            check = c & mask
            if check:
                break 
        a, b = 0, 0
        for i in nums:
            # group A
            if i & mask:
                a = a ^ i
            # group B
            else:
                b = b ^ i
        return [a, b]
                 
            

test = Solution()
nums = [1,2,10,4,7,4,3,3, 6, 7, 6, 1]
# nums = [3, 4, 1, 1]
print(test.singleNumbers(nums))