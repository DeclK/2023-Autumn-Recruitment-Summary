from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # stack
        stack = []
        for i in ops:
            if i == '+':
                new = int(stack[-1]) + int(stack[-2])
                stack.append(new)
            elif i == 'D':
                new = int(stack[-1]) * 2
                stack.append(new)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)

test = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(test.calPoints(ops))