from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        self.ans = []
        def dfs(path, index, target):
            if target < 0: return
            if target == 0:
                self.ans.append(path)
                return
            dfs(path + [candidates[index]], index, target - candidates[index])
            if index < n - 1:
                dfs(path, index + 1, target)

        dfs([], 0, target)
        return self.ans

test = Solution()
candidates = [2,3,1]; target = 6
print(test.combinationSum(candidates, target))