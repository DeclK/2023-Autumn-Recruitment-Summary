class Solution:
    def cuttingRope(self, n: int) -> int:
        from math import sqrt
        m = int(sqrt(n))
        ret = 0
        for m in range(m, n):
            m = m if m > 1 else 2
            num_1 = n // m
            res = n % m    # 有 res 个数字要加1
            unchange = m - res # 有 unchange 个数字不变
            num_2 = num_1 + 1
            ret = max(ret, num_1 ** (m - res) * num_2 ** res)
        return ret 

        
class Solution:
    def cuttingRope(self, n: int) -> int:\
        # 尽可能分为多个长度为 3 的片段
        if n <= 3:
            return n - 1
        num_of_3 = n // 3  # 能否分多少 3 出来
        res = n % 3 # 余数是多少
        if res == 1:
            # 余数为 1 需要把一个 3 分为 2
            num_of_3 -= 1
            return 3 ** (num_of_3) * 4
        elif res == 2:
            return 3 ** (num_of_3) * 2
        else:
            return 3 ** (num_of_3)

        
test = Solution()
n = 120
print(test.cuttingRope(n))