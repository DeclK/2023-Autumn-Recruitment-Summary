class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        def is_valid(str):
            c = Counter(str)
            for r in c.values():
                if r < k:
                    return False
            return True

        def solve(s, k):
            if is_valid(s):
                return len(s)
            counter = Counter(s)
            ans, l, sub = 0, [], ''
            for idx, s_ in enumerate(s):
                if counter[s_] < k:
                    if sub != '':
                        l.append(sub)
                        sub = ''
                elif idx == len(s) - 1:
                    sub += s_
                    l.append(sub)
                else:
                    sub += s_
            for sub_str in l:
                ans = max(ans, solve(sub_str, k))
            return ans
        return solve(s, k)





        # counter = Counter(s)
        # sub_count = {}
        # solution = 0
        # ans = ''

        # for idx, s_ in enumerate(s):
        #     if counter[s_] < k:
        #         if is_valid(sub_count):
        #             solution = max(solution, len(ans))
        #         sub_count = {}
        #         ans = ''
        #     else:
        #         ans += s_
        #         if s_ in sub_count:
        #             sub_count[s_] += 1
        #         else:
        #             sub_count[s_] = 1
        # if is_valid(sub_count):
        #     solution = max(solution, len(ans))
        # return solution


test = Solution()
s = "ababbc"
k = 2
print(test.longestSubstring(s, k))