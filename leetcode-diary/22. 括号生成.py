from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(s):
            stack = []
            for s_ in s:
                if not stack:
                    stack.append(s_)
                else:
                    if s_==')' and stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(s_)
            if stack:
                return False
            else:
                return True
        self.ans = []
        def dfs(path, num_left, num_right):
            if num_left == n:
                path = path + ')' * (n - num_right)
                if is_valid(path):
                    self.ans.append(path)
                return
            if num_right == n:
                path = path + '(' * (n - num_left)
                if is_valid(path):
                    self.ans.append(path)
                return
            dfs(path + '(', num_left + 1, num_right)
            dfs(path + ')', num_left, num_right + 1)
        dfs('', 0, 0)
        return self.ans

test = Solution()
print(test.generateParenthesis(3))