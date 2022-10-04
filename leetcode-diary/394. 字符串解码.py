class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == ']':
                find = len(stack) - 1
                while stack[find] != '[':
                    find -= 1
                # find number
                find_num = find - 1
                while str.isnumeric(stack[find_num]):
                    find_num -= 1
                find_num += 1
                times = stack[find_num: find]
                sub_s = stack[find + 1:]
                stack = stack[:find_num] + sub_s * int(''.join(times))
            else:
                stack.append(s[i])
        return ''.join(stack)

test = Solution()
s = "abc10[cd]xyz"
print(test.decodeString(s))
