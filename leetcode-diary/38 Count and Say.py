class Solution:
    def countAndSay(self, n: int) -> str:
        def desc(s):
            ret = ''
            cur = s[0]
            for idx_, s_ in enumerate(s):
                if s_ == cur[-1]:
                    cur = cur + s_ if idx_ != 0 else s_
                else:
                    ret += str(len(cur)) + cur[0]
                    cur = s_
                if idx_ == len(s) - 1:
                    ret += str(len(cur)) + cur[0]
            return  ret

        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n - 1)
            return desc(s)


test = Solution()
print(test.countAndSay(5))

