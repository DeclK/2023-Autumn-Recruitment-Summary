from typing import List, Tuple
from numpy.core.defchararray import array

from numpy.core.fromnumeric import searchsorted


# class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # solution_1 binary search
    #     def binary_search(list, target):
    #         begin, end = 0, len(list) - 1
    #         while begin <= end:
    #             mid = (begin + end) // 2
    #             if mid == target:
    #                 return True
    #             if list[mid] > target:
    #                 end = mid - 1
    #             else:
    #                 begin = mid + 1
    #         return (end, begin)
    #     for array in matrix:
    #         ret = binary_search(array, target)
    #         if ret:
    #             return True
    #     return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # seach from top right corner
        top_right = matrix[0,-1]
        m, n = len(matrix), len(len(matrix))
        i, j = 0, n - 1
        while i < m and j >= 0:
            top_right = matrix[i][j]
            if top_right == target:
                return True
            elif top_right > target:
                j -= 1
            else:
                i += 1
        return False