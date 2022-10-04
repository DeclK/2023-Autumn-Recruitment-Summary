from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if n < m: return []
        from collections import Counter
        p_dict = Counter(p)
        s_dict = Counter(s[:m])
        ret = []
        for i in range(n - m + 1):
            # judge
            flag = True
            for key in s_dict:
                if s_dict[key] == 0:
                    continue
                if key not in p_dict.keys():
                    flag = False
                    break
                if s_dict[key] != p_dict[key]:
                    flag = False
                    break
            if flag: ret.append(i)

            next_i = i + m
            if next_i < n:
                # update s_dict
                next_s = s[next_i]
                if next_s in s_dict.keys():
                    s_dict[next_s] += 1
                else:
                    s_dict[next_s] = 1
                cur_s = s[i]
                s_dict[cur_s] -= 1
        return ret

test = Solution()
s = "abab"; p = "ab"
print(test.findAnagrams(s, p))
                

