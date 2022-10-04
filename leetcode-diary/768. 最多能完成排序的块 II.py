from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        range_ = [[-1, -1]]
        for num in arr:
            last = range_[-1]
            if num >= last[1]:
                range_.append([num, num])
            else:
                # merge operation
                new_max = range_[-1][1]
                while num < cur_min:
                    # find the min and pop range
                    cur_min = range_[-1][0]
                    if num < cur_min:
                        range_.pop()
                cur_max = range_[-1][1]
                if num >= cur_max:
                    range_.append([num, new_max])
                else:
                    range_[-1][1] = new_max
        return len(range_) - 1
