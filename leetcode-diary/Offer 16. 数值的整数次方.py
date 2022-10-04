class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 重拳出击
        # return x ** n
        # 来一个快速幂 + 位运算
        if n <= 2:
            return x ** n
        if n & 1 == 0:
            return self.myPow(x, n >> 1) ** 2
        else:
            return self.myPow(x, n >> 1) ** 2 * x

test = Solution()
x = 2.1
n = 3
print(test.myPow(x, n))
print(x ** n)