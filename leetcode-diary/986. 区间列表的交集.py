from distutils.command.build_scripts import first_line_re
from tkinter import Listbox
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 纯纯的递归写法
        ans = []
        def solve(list_a, list_b):
            nonlocal ans
            n = len(list_a)
            m = len(list_b)
            if n == 0 or m == 0:
                return
            a = list_a[0]
            b = list_b[0]
            left = max(a[0], b[0])
            right = min(a[1], b[1])
            if left <= right:
                ans.append([left, right])
            if a[1] < b[1]:
                list_a.pop(0)
            else: list_b.pop(0)
            solve(list_a, list_b)
        solve(firstList, secondList)
        return ans

test = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
firstList = [[1,3],[5,9]]
secondList = []
print(test.intervalIntersection(firstList, secondList))