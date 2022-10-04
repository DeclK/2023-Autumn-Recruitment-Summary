from typing import List

from cv2 import merge


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 和重叠区间一题有相似之处
        # 先对区间进行排序, 考虑相邻两个区间, 看是否能够融合, 如果不能够融合
        # 则考虑下一个相邻区间
        inter = sorted(intervals)
        print(inter )
        n = len(inter)
        if n == 1: return [intervals[0]]
        ret = [list(inter[0])]
        for i in range(1, n):
            inter1 = ret[-1]
            inter2 = inter[i]
            left = max(inter1[0], inter2[0])
            right = min(inter1[1], inter2[1])
            if left <= right:   # 判断是否重叠
                new_iter = [inter1[0], max(inter1[1], inter2[1])]
                ret.pop()
                ret.append(new_iter)
            else:
                ret.append(list(inter2))
        return ret

test = Solution()
intervals = [[1,20],[8,10],[2, 6],[15,18]]
print(test.merge(intervals))