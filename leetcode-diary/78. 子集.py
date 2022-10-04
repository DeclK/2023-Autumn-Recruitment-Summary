from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        def dfs(path, i):
            if i == n:
                self.ans.append(path)
                return
            dfs(path + [nums[i]], i + 1)
            dfs(path, i + 1)
        dfs([], 0)
        return self.ans

nums =[1,2,3]
test= Solution()
print(test.subsets(nums))