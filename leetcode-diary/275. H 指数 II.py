from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 二分查找
        n = len(citations)
        right = n - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            value = citations[mid]
            if value >= (n - mid):
                right = mid - 1
            else:
                left = mid + 1
        return n - left

test = Solution()
citations = sorted([3,0,6,1,5])
citations = [1]
print(test.hIndex(citations))

        