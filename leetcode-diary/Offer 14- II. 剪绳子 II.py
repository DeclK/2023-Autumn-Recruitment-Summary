from turtle import numinput


class Solution:
    def cuttingRope(self, n: int) -> int:
        # 不想思考了，直接穷举
        def calculate(n, m):
            num_1 = n // m
            res = n % m # res 个数要 +1
            unchange = m - res  # unchange 不变
            return (num_1 ** (unchange) * (num_1 + 1) ** res) % mod
        ret = 0
        mod = 10 ** 9 + 7
        for m in range(2, n + 1):
            ret = max(ret, calculate(n, m))
        return ret

test = Solution()
n = 120
print(test.cuttingRope(n))