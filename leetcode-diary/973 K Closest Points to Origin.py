from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)
        
        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans

test =Solution()
points = [[1,3],[-2,2]]
K = 1
print(test.kClosest(points, K))