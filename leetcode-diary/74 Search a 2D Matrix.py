from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        import numpy as np
        sum_col = sum(colsum)
        n = len(colsum)
        if sum_col - lower != upper or upper > n:
            return []
        mark_2 = np.array(colsum) == 2
        sum_ = mark_2.sum()
        if sum_ > lower:
            return []
        upper -= sum_
        a = np.zeros((2, n), dtype=np.int)
        for i in range(n):
            if mark_2[i] == True:
                continue
            if colsum[i] > 0 and upper > 0:
                a[0, i] = 1
                upper -= 1
            a[1, i] = colsum[i] - a[0, i]
        return a.tolist()