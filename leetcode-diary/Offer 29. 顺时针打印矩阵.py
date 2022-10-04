from operator import le
from re import search
from turtle import left
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 直接使用循环
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        direction_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0] * n for i in range(m)]
        ret = []
        i, j = 0, 0
        def is_valid(i, j):
            if 0<= i < m and 0 <= j < n and visited[i][j] == 0:
                return True
            return False
        while is_valid(i, j):
            for idx, (a, b) in enumerate(direction_list):
                while is_valid(i, j):
                    ret.append(matrix[i][j])
                    visited[i][j] = 1
                    i, j = i + a, j + b
                if idx < 3:
                    i = i + direction_list[idx + 1][0] - a
                    j = j + direction_list[idx + 1][1] - b
                else:
                    i = i + direction_list[0][0] - a
                    j = j + direction_list[0][1] - b
        return ret

test = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1]]
print(test.spiralOrder(matrix))