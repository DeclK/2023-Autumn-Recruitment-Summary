class Solution:
    def add(self, a: int, b: int) -> int:
        pre = 0
        ans = 0
        for i in range(32):
            mask = 1 << i
            num0, num1 = a & mask, b & mask
            num = num0 ^ num1 ^ pre
            ans = ans | num
            if num1 and num0 or num1 and pre or num0 and pre:
                pre = 1 << (i + 1)
            else: pre = 0
        # print(bin(ans))
        # print(ans)
        # print(~(ans ^ 0xffffffff))
        if ans < (1 << 32 - 1): return ans
        else: return ~(ans ^ 0xffffffff)

test = Solution()
a = 1
b = -2
print(test.add(a, b))