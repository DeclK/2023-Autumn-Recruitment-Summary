class Solution:
    def strToInt(self, str: str) -> int:
        # 1. 第一个非空字符不是数字正负号则返回 false
        # 2. 舍弃掉空格和其他数字
        # 先返回一个只有 + - number 的字符串，然后判断
        ans = ''
        sym = False
        first = False
        for i in str:
            if sym == False and (i == '+' or i == '-') and ans == '':
                ans += i
                sym == True
                first = True
            elif i in '0123456789.':
                ans += i
                first = True
            elif first == False and i != ' ': return 0
        if ans == '' or ans == '+' or ans == '-': return 0
        ans = int(float(ans))
        if -2**31 <= ans <= 2**31 - 1: return ans
        elif ans > 2**31 - 1: return 2**31 - 1
        else: return -2**31

test = Solution()
str =  " "
print(test.strToInt(str))