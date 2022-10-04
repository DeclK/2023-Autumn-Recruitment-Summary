class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 一边 pair 一边计数，难点是如何判断连续
        # 将无法配对的括号标记出来，之后计算其间隔即可
        sub_ans = 0
        ans = 0
        n = len(s)
        stack = []
        for idx, i in enumerate(s):
            if i == '(':
                stack.append([i, idx])
            else:
                if len(stack) > 0 and stack[-1][0] == '(':
                    sub_ans += 1
                    stack.pop()
                else:
                    stack.append([i, idx])
        stack.append([None, n])
        stack.insert(0, [None, -1])
        step = [stack[idx + 1][1] - stack[idx][1] for idx in range(len(stack) - 1)]
        return max(step) - 1 

test = Solution()
s = "(()"
print(test.longestValidParentheses(s))

