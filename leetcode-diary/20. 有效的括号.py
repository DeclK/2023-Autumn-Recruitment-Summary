class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def check(s1, s2):
            if s1 == '(' and s2 == ')': return True
            if s1 == '{' and s2 == '}': return True
            if s1 == '[' and s2 == ']': return True
            return False
        for s_ in s:
            if not stack:
                stack.append(s_)
            else:
                if check(stack[-1], s_):
                    stack.pop()
                else:
                    stack.append(s_)
        if stack:
            return False
        else:
            return True