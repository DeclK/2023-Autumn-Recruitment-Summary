from typing import List

from pyrsistent import pset


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 尝试暴力解法
        p_set = set(map(tuple, points))
        points = sorted(points)
        n = len(points)
        def check(point):
            return point in p_set
        ans = 1e10
        for i in range(n):
            p1 =  points[i]
            for j in range(i + 1, n):
                p2 =  points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    p3 = (p1[0], p2[1])
                    p4 = (p2[0], p1[1])
                    if check(p3) and check(p4):
                        width = abs(p1[0] - p2[0])
                        height = abs(p1[1] - p2[1])
                        ans = min(ans, width * height)
        return ans if ans < 1e10 else 0

test = Solution()
points = [[0,1],[3,2],[5,5],[4,5],[4,4],[2,0],[2,3],[2,2],[1,0],[5,1],[2,5],[5,2],[2,4],[4,0]]
print(test.minAreaRect(points))

