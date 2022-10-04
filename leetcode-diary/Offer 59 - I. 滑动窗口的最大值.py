import collections
import enum
import heapq
from re import A
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 想不出 O(N) 时间复杂度，先实现暴力
        que = collections.deque()
        ans = []
        for i in nums:
            que.append(i)
            if len(que) == k:
                ans.append(max(que))
                que.popleft()
        return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 试一试堆
        heap = [(-num, idx) for idx, num in enumerate(nums) if idx < k - 1]
        heapq.heapify(heap)
        ans = []
        for idx in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[idx], idx))
            while True:
                top, top_index = heap[0]
                if idx - k < top_index <= idx:
                    ans.append(-top)
                    break
                else: heapq.heappop(heap)
        return ans
                
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列
        if not nums: return []
        ans = []
        que = collections.deque()
        for idx, i in enumerate(nums):
            if que and idx - que[0][1] >= k:
                que.popleft()
            while que and i > que[-1][0]:
                que.pop()
            que.append((i, idx))
            if idx >= k - 1: ans.append(que[0][0])
        return ans

test = Solution()
nums = [1,3,1,2,0,5]
k = 3
print(test.maxSlidingWindow(nums, k))