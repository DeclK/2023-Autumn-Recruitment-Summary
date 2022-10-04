from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_in = [0] * (n + 1)     # buy in status maxi
        dp_out = [0] * (n + 1)    # buy out status maxi
        dp_cold = [0] * (n + 1)   # cold status maxi
        dp_in[1] = -prices[0]
        ret = 0
        for i in range(2, n + 1):
            index_i = i - 1
            dp_in[i] = max(dp_out[i - 1] - prices[index_i], dp_in[i - 1])
            dp_out[i] = max(dp_out[i - 1], dp_cold[i - 1])
            dp_cold[i] = dp_in[i - 1] + prices[index_i]
            ret = max(ret, dp_in[i], dp_out[i], dp_cold[i])
        return ret

test = Solution()
prices = [1]
print(test.maxProfit(prices))
