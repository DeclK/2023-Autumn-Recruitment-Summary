from typing import Tuple


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def is_legal(s, d):
            d_s = dict.fromkeys(s, 1)
            return d_s == d
        def recur(s, d):
            if len(s) == 1:
                d_ = dict.fromkeys(s, 1)
                # minimum = s if is_legal(s, d) else 1e10
                minimum = s
                return s, d_, minimum
            else:
                ret_, d_, minimum = recur(s[1:], d)
                if d_.get(s[0], None):
                    min_ = minimum.replace(s[0], '')
                    ret_ = s[0] + min_
                    minimum = min(ret_, minimum)
                    return ret_, d_, minimum
                else:
                    d_[s[0]] = 1
                    minimum = s[0] + minimum
                    return ret_, d_, minimum
        d = dict.fromkeys(s, 1)
        return recur(s, d)[2]




test = Solution()
s = "abacb"
print(test.removeDuplicateLetters(s))