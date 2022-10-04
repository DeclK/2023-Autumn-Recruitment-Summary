from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        far = [i + nums[i] for i in range(n)]
        farthest = -1
        for idx, d in enumerate(far):
            if d > farthest:
                farthest = d
            if idx < farthest:
                continue
            if idx == farthest or farthest >= n - 1:
                break
        if farthest >= n - 1: return True
        return False


test = Solution()
nums = [2,3,1,1,4]
print(test.canJump(nums))