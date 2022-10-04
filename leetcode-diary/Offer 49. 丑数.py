from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 首先考虑使用堆方法
        nums = [1]
        count = 0
        pre = 0
        d = {}
        while count < n:
            num = heappop(nums)
            if d.get(num * 2, None) == None: 
                heappush(nums, num * 2)
                d[num * 2] = 1
            if d.get(num * 3, None) == None: 
                heappush(nums, num * 3)
                d[num * 3] = 1
            if d.get(num * 5, None) == None: 
                heappush(nums, num * 5)
                d[num * 5] = 1
            if num == pre: continue
            count += 1
        return num

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 动态规划
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[i] == dp[a] * 2: a += 1
            if dp[i] == dp[b] * 3: b += 1
            if dp[i] == dp[c] * 5: c += 1
        return dp[n - 1]

test = Solution()
n = 359
print(test.nthUglyNumber(n))
