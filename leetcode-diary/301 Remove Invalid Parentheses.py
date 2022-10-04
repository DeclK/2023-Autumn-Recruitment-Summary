from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 依然先使用栈匹配括号，注意字母的情况
        n = len(s)
        def is_valid(s):
            # 返回栈中的数字
            stack = []
            for idx, i in enumerate(s):
                if i == '(':
                    stack.append(idx)
                elif i == ')':
                    if len(stack) > 0 and s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(idx)
            return stack
        idx_to_delete = is_valid(s)
        ans = set()
        def dfs(path, idx, d):
            # 深度搜索，并返回结果
            if d == 0:
                check = path + s[idx:]
                if len(is_valid(check)) == 0:
                    ans.add(check)
                return
            elif (n - idx) < d:
                return
            elif s[idx] != ')' and s[idx] != '(':
                dfs(path + s[idx], idx + 1, d)
            else:
                dfs(path + s[idx], idx + 1, d)
                dfs(path, idx + 1, d - 1)
        dfs('', 0, len(idx_to_delete))
        return list(ans)


    
test = Solution()
s = "(((k()(("
print(test.removeInvalidParentheses(s))