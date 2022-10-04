import enum
from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        import numpy as np
        all_p = [p1, p2, p3, p4]
        points = []
        for p in all_p:
            points.append(np.array(p))
        l1 = points[1] - points[0]
        l2 = points[2] - points[0]
        l3 = points[3] - points[0]
        len1 = np.linalg.norm(l1)
        len2 = np.linalg.norm(l2)
        len3 = np.linalg.norm(l3)
        
        sort_len = np.sort([len1, len2, len3])
        arg_sort = np.argsort([len1, len2, len3])

        if sort_len[0] != sort_len[1]: return False
        # check angle
        p0 = points[0]
        p1 = points[arg_sort[0] + 1]
        p2 = points[arg_sort[1] + 1]
        l1 = p1 - p0
        l2 = p2 - p0
        if np.dot(l1, l2) != 0: return False

        p3 = points[arg_sort[2] + 1]
        l3 = p3 - p0
        check = l3 - (l1 + l2)
        if np.sum(check) != 0: return False
        if np.linalg.norm(l3) == 0: return False

        return True
        

test = Solution()
p1 = [0,0]; p2 = [1,1]; p3 = [1,0]; p4 = [0,1]
p1 = [0,0]; p2 = [1,1]; p3 = [1,0]; p4 = [0,12]
print(test.validSquare(p1,p2,p3,p4))
        