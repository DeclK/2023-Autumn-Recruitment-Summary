from typing import List

from tqdm import trange

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            if i == 0:
                continue
            for j in range(len(triangle[i])):
                if j == 0:
                    right = triangle[i][j] + triangle[i - 1][j]
                    triangle[i][j] = right
                elif j == i - 1 + 1:
                    left = triangle[i][j] + triangle[i - 1][j -1]
                    triangle[i][j] = left
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

test = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(test.minimumTotal(triangle))

