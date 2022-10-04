class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d_s = dict.fromkeys(list(s), None)
        d_t = dict.fromkeys(list(t), None)
        flag = True
        for idx, s_ in enumerate(s):
            t_, ds, dt = t[idx], d_s[s_], d_t[t_]
            if ds is None and dt is None:
                d_s[s_], d_t[t_] = t_, s
            elif ds and dt:
                if ds != t_ or dt != s:
                    flag = False
                    break
            else:
                return False
        return flag

s = "EGG"
t = "ABB"
test = Solution()
print(test.isIsomorphic(s, t))