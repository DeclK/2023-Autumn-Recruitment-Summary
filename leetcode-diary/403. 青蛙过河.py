from typing import List

from torch import det


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp[i][2] 第 i 个石头的状态
        # 0: 能够到达 1: 能够到达的步长 k
        n = len(stones)
        d = {val: idx for idx, val in enumerate(stones)}
        dp = [[False, []] for i in range(n)]
        dp[0][0] = True
        dp[0][1].append(1)
        for i in range(n):
            if dp[i][0]:
                step = set()
                for k in dp[i][1]:
                    if i == 0: step.add(1)
                    else:
                        step.add(k + 1)
                        step.add(k - 1)
                        step.add(k)
                for step_ in step:
                    dest = step_ + stones[i]
                    if d.get(dest):
                        index = d[dest]
                        dp[index][0] = True
                        dp[index][1].append(step_)
        return dp[n - 1][0]

test = Solution()
stones = [0, 2, 3]
print(test.canCross(stones))

