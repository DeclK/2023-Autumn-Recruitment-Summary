from turtle import st
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 二分查找
        citations = sorted(citations, reverse=True)
        def check(x):
            # 是否存在 x 篇大于等于 x 的
            if x >= 1 and citations[x - 1] >= x: return True
            return False
        left = 1
        right = len(citations)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 使用一个数组存储 store[i + 1] 代表值为 i 的次数
        # store[n] 代表 >= n 的次数
        n = len(citations)
        store = [0] * (n + 1)
        for i in citations:
            pos = i % (n + 1)
            check = i // n
            if check >= 1:
                store[-1] += 1
            else:
                store[pos] += 1 
        ans = 0
        for i in range(n, 0, -1):
            if store[i] >= i:
                ans = i
                break
            else:
                store[i - 1] += store[i]
        return ans



test = Solution()
citations = [3,0,6,1,5]
# citations = [1]
print(test.hIndex(citations))
