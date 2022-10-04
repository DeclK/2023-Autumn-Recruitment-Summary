from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {}
        count, s_ = 0, 0
        for i in range(n):
            # 前缀和
            s_ += nums[i]
            # 检查 sum 自身是否等于
            if s_ == k:
                count += 1
            # 检查当前 sum_ 是否是别人的期待
            count += d.get(s_, 0)
            # 将当前期待更新到字典
            new_target = s_ + k
            d[new_target] = d.get(new_target, 0) + 1
        return count
            
test = Solution()
k = 0
nums = [1, 1, 0]
print(test.subarraySum(nums, k))