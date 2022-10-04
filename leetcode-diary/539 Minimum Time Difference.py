from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_time_list(timePoints):
            for i in range(len(timePoints)):
                time = list(map(int,timePoints[i].split(':')))
                time = time[0] * 60 + time[1]
                timePoints[i] = time
            return timePoints
        def get_diff(t1, t2):
            return min(abs(t1-t2), -abs(t1-t2) + 24 * 60)

        t_list = sorted(get_time_list(timePoints))
        minimum = get_diff(t_list[0], t_list[-1])
        for i in range(len(t_list) - 1):
            minimum = min(minimum, get_diff(t_list[i], t_list[i+1]))
            if minimum == 0:
                return 0
        return minimum

test = Solution()
timePoints = ["00:00","04:00","22:00"]
print(test.findMinDifference(timePoints))