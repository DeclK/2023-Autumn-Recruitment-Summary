from typing import List

from torch import le


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            if height[left] > height[right]:
                ans = max(ans, height[right] * (right - left))
                right -= 1
            else:
                ans = max(ans, height[left] * (right - left))
                left += 1
        return ans
