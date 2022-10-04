from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up, left = i - 1, j - 1
                if up < 0:
                    grid[i][j] += grid[i][left]
                elif left < 0:
                    grid[i][j] += grid[up][j]
                else:
                    grid[i][j] += min(grid[up][j],grid[i][left])
        return grid[m-1][n-1]
                
grid = [[1,2,3],[4,5,6]]
test = Solution()
print(test.minPathSum(grid))