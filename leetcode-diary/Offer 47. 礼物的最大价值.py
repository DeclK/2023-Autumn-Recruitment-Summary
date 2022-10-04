from re import search
from sre_constants import GROUPREF_IGNORE
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 为什么一开始想着去搜索了呢！
        m = len(grid)
        if m == 0: return
        n = len(grid[0])
        def is_valid(i, j):
            if 0 <= i < m and 0 <= j < n: return True
            else: return False
        ans = 0
        def dfs(i, j, val):
            nonlocal ans
            if i == m - 1 and j == n - 1:
                ans = max(ans, val + grid[i][j])
                return
            search_list = [[i + 1, j], [i, j + 1]]
            for i_, j_ in search_list:
                if is_valid(i_, j_):
                    dfs(i_, j_, val + grid[i][j])
        dfs(0, 0, 0)
        return ans

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 应该使用动态规划啊！
        # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
        m = len(grid)
        if m == 0: return
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j != 0: grid[i][j] = grid[i][j - 1] + val
                elif j == 0 and i != 0: grid[i][j] = grid[i - 1][j] + val
                elif i == 0 and j == 0:continue
                else:
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + val
        return grid[m - 1][n - 1]
test = Solution()
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(test.maxValue(grid))