from math import ceil


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n == 0:return 0
        num = 0
        pre = 0
        digit = 1
        while n > num:
            pre = num
            num += digit * (9 * 10 ** (digit - 1))
            digit += 1
        res = n - pre - 1
        digit -= 1
        count = res // (digit)
        number  = 10 ** (digit - 1) + count
        rest = res % digit
        return int(str(number)[rest])

    def findNthDigit(self, n):
        digit = 1
        count = 0
        pre_count = 0
        while n >= count:  
            # number of digit <= digit
            pre_count = count
            count += digit * 9 * 10 ** (digit - 1)
            digit += 1
        extra = n - pre_count
        digit -= 1 
        base = 10 ** (digit - 1) - 1
        number = base + (n - 1) // digit + 1    # ceil operation
        rest = extra % digit
        ret = str(number)[rest - 1]
        return int(ret)

test = Solution()
n = 3
print(test.findNthDigit(n))