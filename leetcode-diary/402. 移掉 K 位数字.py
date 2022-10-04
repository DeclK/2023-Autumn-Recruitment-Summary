import numbers
import random


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        if k >= n: return '0'
        count = 0
        for i in range(n):
            if not stack:
                stack.append(num[i])
                continue
            while count < k and stack and num[i] < stack[-1]:
                stack.pop()
                count += 1
            stack.append(num[i])
        ans = ''.join(stack)[:n - k]
        return ans.lstrip('0')

test = Solution()
num = '77'
k = 1
# num = random.randint(1, 100)
# num = str(num)
# print(num)
# num = '19114'
# num = "120200"
# k = 3
print(test.removeKdigits(num, k))