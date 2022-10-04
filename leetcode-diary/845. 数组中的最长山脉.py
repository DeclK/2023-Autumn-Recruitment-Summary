from tabnanny import check
from typing import List

from cv2 import SOLVELP_UNBOUNDED


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 这一题不就是最长回文字串吗，不过没有对称而已
        n = len(arr)
        dp = [[False] * n for i in range(n)]
        ans = -1
        # dp[i][j] = dp[i + 1][j - 1] is True & arr[i] arr[j] < arr[i + 1] arr[j - 1]
        # dp[i][j] = dp[i + 1][j] is True and arr[i] < arr[i + 1]
        # 考虑边界情况
        def check(i):
            return 0 < i < n - 1
        for j in range(n):
            if check(j):
                if arr[j + 1] < arr[j] > arr[j - 1]:
                    dp[j - 1][j + 1] = True
            # dp[j][j] = True
            for i in range(j - 2, -1, -1):
                if i > j - 2: continue
                if dp[i + 1][j]:
                    if arr[i + 1] > arr[i]:
                        dp[i][j] = True
                        ans = max(ans, j - i + 1)
                if dp[i][j - 1]:
                    if arr[j - 1] > arr[j]:
                        dp[i][j] = True
                        ans = max(ans, j - i + 1)
        return max(ans, 0)

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 上面的动态规划超时了考虑使用栈维护
        n = len(arr)
        if n < 3: return 0
        ans = 0
        # 第一个上升点
        stack = [arr[0]]
        count = 0   # 有无峰
        status = 0  # 有无上坡
        for i in range(0, n):
            # 当为升序时
            if arr[i] > stack[-1] and count == 0:
                stack.append(arr[i])
                status = 1
            elif arr[i] > stack[-1] and count == 1:
                ans = max(ans, len(stack))
                stack = [stack[-1], arr[i]]
                count = 0
            # 当为降序时
            elif arr[i] < stack[-1]:
                if status == 1:
                    stack.append(arr[i])
                    count = 1
                else:
                    stack = [arr[i]]
                    status = 0
                    count = 0
            # 当与之前相等时
            elif arr[i] == stack[-1]:
                if count == 1: ans = max(ans, len(stack))
                stack = [arr[i]]
                count = 0
                status = 0
        if count == 1: ans = max(ans, len(stack))
        return ans

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 三次动态规划解决
        # 左侧可扩展的数字

        n = len(arr)
        if n < 3: return 0
        left = [0] * n
        # left[i] = left[i - 1] + 1 if arr[i] > arr[i - 1] else 0
        right = [0] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1 
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
        ans = 0
        for i in range(n):
            if left[i] != 0 and right[i] != 0:
                ans = max(ans, left[i] + right[i] + 1)
        return ans 


test = Solution()
arr = [1 ,2,2,-1]
# arr = [5, -1, 0, 3, 2, 0, -1, -2, 4, 3]
print(test.longestMountain(arr))