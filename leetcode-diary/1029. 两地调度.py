from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 假设全部都去某一个地方, 然后再进行挑选, 看怎样能够减少更多的钱
        diff = [m[1] - m[0] for m in costs]
        n = len(costs)
        cur_sum = 0
        for m in costs:
            cur_sum += m[0]
        sort_diff = sorted(diff)
        for i in range(n // 2):
            cur_sum += sort_diff[i]
        return cur_sum

test = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
print(test.twoCitySchedCost(costs))
        
