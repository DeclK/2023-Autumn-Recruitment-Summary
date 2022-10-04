from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        counter = Counter(candidates)
        uniq_cand = sorted(counter)
        ans = []
        def dfs(pos, sub_ans: List, target):
            if target == 0:
                ans.append(sub_ans)
                return
            if pos == len(uniq_cand) or uniq_cand[pos] > target:
                return

            for pos_ in range(pos, len(uniq_cand)):
                num = uniq_cand[pos_]
                freq = counter[num]
                repeat = min(freq, target // num)
                for r_ in range(1, repeat + 1):
                    # 不再考虑 sub_ans 改变的事情
                    # sub_ans_copy = sub_ans.copy()
                    # sub_ans_copy += [num] * r_
                    dfs(pos_ + 1, sub_ans + [num] * r_, target - num * r_)
        dfs(0, [], target)
        return ans
                

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        uniq_cand = sorted(Counter(candidates).items())
        ans = []
        sub_ans = []
        def dfs(pos, target):
            nonlocal sub_ans
            if target == 0:
                ans.append(sub_ans[:])
                return
            if pos == len(uniq_cand) or uniq_cand[pos][0] > target:
                return

            for pos_ in range(pos, len(uniq_cand)):
                num = uniq_cand[pos_][0]
                freq = uniq_cand[pos_][1]
                repeat = min(freq, target // num)
                for r_ in range(1, repeat + 1):
                    sub_ans += [num] * r_
                    dfs(pos_ + 1, target - num * r_)
                    sub_ans[:] = sub_ans[:-r_]
        dfs(0, target)
        return ans

test = Solution()
candidates =[14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
# candidates = [1,1,1,2]
target = 27
print(test.combinationSum2(sorted(candidates), target))