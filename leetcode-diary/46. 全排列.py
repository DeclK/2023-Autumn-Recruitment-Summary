from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ans = []
        def dfs(path, choice:list):
            if len(path) == n:
                self.ans.append(path)
            m = len(choice)
            for i in range(m):
                dfs(path + [choice[i]], choice[:i] + choice[i+1:])
        dfs([], nums)
        return self.ans

test = Solution()
nums = [1, 2, 3]
print(test.permute(nums))