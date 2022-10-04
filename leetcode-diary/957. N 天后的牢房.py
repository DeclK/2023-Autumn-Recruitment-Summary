from typing import List

from cairo import Status


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # 这一题比较有意思, 因为牢房房间数是固定的
        # 说明有固定状态的牢房房间, 仅仅有 2**6 种变化
        day1 = [0] * 8
        for i in range(1, 7):
            if cells[i - 1] == cells[i + 1]:
                day1[i] = 1
            else:
                day1[i] = 0
        if n == 1: return day1
        status = {}
        next_day = day1[:]
        while status.get(tuple(next_day)) is None:
            status[tuple(next_day)] = 1
            for i in range(1, 7):
                if day1[i - 1] == day1[i + 1]:
                    next_day[i] = 1
                else:
                    next_day[i] = 0
            day1 = next_day[:]
        N = len(status)
        count = (n - 1) % N + 1
        for key in status:
            count -= 1
            if count == 0:
                return list(key)

test = Solution()
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(test.prisonAfterNDays(cells, N))

            

