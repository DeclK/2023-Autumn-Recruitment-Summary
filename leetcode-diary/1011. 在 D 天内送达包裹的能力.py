from re import template
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 二分查找
        # 假设穿的重量为 x, 能够在 days 内返回的可能
        def check(x):
            count = 1
            tempt = 0
            for i in weights:
                tempt += i
                if tempt > x:
                    count += 1
                    tempt = i
            if count <= days: return True
            else: return False
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

test = Solution()
weights = [3,2,2,4,1,4]
days = 3
# days = 5
print(test.shipWithinDays(weights, days))
