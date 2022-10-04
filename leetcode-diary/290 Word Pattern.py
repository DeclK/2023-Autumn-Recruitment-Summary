class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(s_list) != len(pattern):
            return False
        pattern_dict = dict.fromkeys(list(pattern), None)
        s_dict = dict.fromkeys(s_list, None)
        print(list(map(pattern.index, pattern)))
        for idx, s_ in enumerate(s_list):
            p_ = pattern[idx]
            p_d = pattern_dict[p_]
            s_d = s_dict[s_]
            if p_d is None and s_d is None:
                pattern_dict[p_] = s_
                s_dict[s_] = p_
            elif p_d and s_d:
                if p_d != s_ or s_d != p_:
                    return False
            else:
                return False
        return True

pattern = "abba"
str = "dog cat cat dog"
test = Solution()
print(test.wordPattern(pattern, str))