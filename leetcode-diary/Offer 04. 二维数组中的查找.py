# 这一题之前做过
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >=0:
            if target < matrix[i][j]:
                j = j - 1
            elif target > matrix[i][j]:
                i = i + 1
            else:
                return True
        return False