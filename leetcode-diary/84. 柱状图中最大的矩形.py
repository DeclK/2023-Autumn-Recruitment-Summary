from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 这一题和接雨水比较类似
        # 对于每一个柱子, 寻找左右侧最近低于自己的柱子
        # 但是接雨水是使用的左右侧的最大值, 而上述情况就是使用单调栈的典型情况
        heights = [0] + heights + [0]
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n):
            while stack and stack[-1][0] > heights[i]:
                present = stack[-1]
                previous = stack[-2]
                sub = (i - previous[1] - 1) * present[0]
                ans = max(ans, sub)
                stack.pop()
            stack.append((heights[i], i))
        return ans

test = Solution()
heights = [2,3 ,4 ,3]
print(test.largestRectangleArea(heights))
            
