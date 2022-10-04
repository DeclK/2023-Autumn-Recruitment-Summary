class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        def move_one(s):
            n = len(s)
            ret = s
            for i in range(n):
                new_s = s[i:] + s[:i]
                ret = min(ret, new_s)
            return ret
        if k == 1:
            return move_one(s)
        else:
            l = list(s)
            l = sorted(l)
            return ''.join(l)

test = Solution()
s = 'baaca'
k = 3
print(test.orderlyQueue(s, k))