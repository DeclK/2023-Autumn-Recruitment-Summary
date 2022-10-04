from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 据说也是商汤会考的做一下
        # 首先想到的是使用递归
        n = len(matrix)
        if n == 0: return 
        r_times = n // 2
        def rota(left_top):
            if left_top >= r_times: return
            # 4 positions (corners)
            lu = [left_top, left_top]
            ru = [left_top, n - left_top - 1]
            ld = [n - left_top - 1, left_top]
            rd = [n - left_top - 1, n - left_top - 1]
            times = n - 2 * left_top - 1
            for _ in range(times):
                matrix[lu[0]][lu[1]], matrix[ru[0]][ru[1]], matrix[rd[0]][rd[1]], matrix[ld[0]][ld[1]] \
            =   matrix[ld[0]][ld[1]], matrix[lu[0]][lu[1]], matrix[ru[0]][ru[1]], matrix[rd[0]][rd[1]]
                lu[1] += 1
                ru[0] += 1
                ld[0] -= 1
                rd[1] -= 1  
            rota(left_top + 1)
        rota(0)
        return matrix

test = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(test.rotate(matrix))