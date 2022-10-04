from typing import List

from sympy import solve


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def solve(array):
            array = array + [0]
            n = len(array)
            stack = []
            ans = 0
            for i in range(n):
                while stack and stack[-1][0] > array[i]:
                    if len(stack) == 1:
                        sub_ans = i * stack[-1][0]
                    else:
                        sub_ans = (i - stack[-2][1] - 1) * stack[-1][0]
                    ans = max(ans, sub_ans)
                    stack.pop()
                stack.append((array[i], i))
            return ans

        # 按照层来进行循环
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        array = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    array[j] = 0
                else:
                    array[j] = array[j] + matrix[i][j]
            sub_ans = solve(array)
            ans = max(sub_ans, ans)
        return ans

test = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["1","0","0","0","1"],["1","1","0","1","1"],["1","1","1","1","1"]]

print(test.maximalRectangle(matrix))