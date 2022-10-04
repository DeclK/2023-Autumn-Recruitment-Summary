from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visit = [[False] * m for _ in range(n)]
        def dfs(i, j):
            if i == n or j == m or i == -1 or j == -1: return False
            if visit[i][j]: return False
            if grid[i][j] == '0': return False
            visit[i][j] = True
            search_list = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for i_, j_ in search_list:
                dfs(i_, j_)
            return True
        counter = 0
        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    counter += 1
        return counter

