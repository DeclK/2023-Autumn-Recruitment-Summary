from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol = ['+', '-', '*', '/']
        stack = []
        for input in tokens:
            if input in symbol:
                b = stack.pop()
                a = stack.pop()
                if input == '+':
                    c = a + b
                elif input == '-':
                    c = a - b
                elif input == '*':
                    c = a * b
                else:
                    c = a // b
                    if a % b != 0:
                        c = c if c >= 0 else c + 1
                stack.append(c)
            else:
                stack.append(int(input))
        return stack[-1]

test = Solution()
tokens = ["4","-2","/","2","-3","-","-"]
print(test.evalRPN(tokens))

