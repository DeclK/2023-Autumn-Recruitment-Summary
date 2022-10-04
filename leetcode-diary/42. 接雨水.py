from turtle import left, right
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 两次动态规划, 知道左右侧最大即可
        n = len(height)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            if i == 0: left[i] = height[i]
            else:
                left[i] = max(left[i - 1], height[i - 1])
        for i in range(n - 1, -1, -1):
            if i == n - 1: right[i] = height[i]
            else:
                right[i] = max(right[i + 1], height[i + 1])
        ans = 0
        for i in range(1, n - 1):
            bound = min(left[i], right[i])
            ans += max(bound - height[i], 0)
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        # 使用 O(1) 的双指针
        n = len(height)
        left = 0
        left_maxi = height[left]
        right = n - 1
        right_maxi = height[right]
        ans = 0
        while left < right:
            if height[left] < height[right]:
                # 判断是否能蓄水
                bound = min(left_maxi, right_maxi)
                ans += max(bound - height[left], 0)
                left += 1
                left_maxi = max(left_maxi, height[left])
            else:
                bound = min(left_maxi, right_maxi)
                ans += max(bound - height[right], 0)
                right -= 1
                right_maxi = max(right_maxi, height[right])
        return ans 

                

test = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(test.trap(height))
