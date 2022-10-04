from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 从头遍历，并用一个 counter 进行辅助
        counter = Counter(s)
        for i in s:
            if counter[i] == 1:
                return i
        return ""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d: d[i] = False
            else: d[i] = True
        for key, val in d.items():
            if val: return key
        return " "

test = Solution()
s = "abaccdeff"
print(test.firstUniqChar(s))