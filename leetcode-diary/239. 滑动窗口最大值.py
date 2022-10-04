import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 版本1 堆
        window = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(window)
        ans = []
        n = len(nums)
        for i in range(k - 1, n):
            heapq.heappush(window, (-nums[i], i))
            index = i - k
            while window[0][1] <= index:
                heapq.heappop(window)
            ans.append(-window[0][0])
        return ans


test = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(test.maxSlidingWindow(nums, k))
