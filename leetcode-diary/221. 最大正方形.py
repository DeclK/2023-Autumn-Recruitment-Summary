from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # check the position is the right bottom of the largest square
        # it is decided by 3 parts: 1. upper status 2. vertical 3. horizontal
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        ret = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    else:
                        dp[i][j] = 1
                    ret = max(ret, dp[i][j])
        return ret ** 2

test = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(test.maximalSquare(matrix))