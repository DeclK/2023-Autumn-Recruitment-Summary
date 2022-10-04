from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = [0] * n
        m = -1e3
        ans = 0
        for i in range(n - 1, -1, -1):
            if prices[i] > m:
                maxi[i] = prices[i]
                m = prices[i]
            else: maxi[i] = m
            ans = max(ans, maxi[i] - prices[i])
        return ans

test = Solution()
prices = [7,6,4,3,1]
print(test.maxProfit(prices))