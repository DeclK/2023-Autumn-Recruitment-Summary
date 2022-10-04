class Solution:
    def countDigitOne(self, n: int) -> int:
        ret = 0
        i = 0
        num = n
        while num:
            cur = num % 10
            high = num  // 10
            low = n % (10 ** i)
            if cur == 0: ret += high * 10 ** i
            elif cur == 1: ret += high * 10 ** i + low + 1
            else: ret += (high + 1) * 10 ** i
            num = high
            i += 1
        return ret

test = Solution()
n = 101
print(test.countDigitOne(n))