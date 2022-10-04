from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        look_up = {num: idx for idx, num in enumerate(nums)}
        ans = set()
        ret = []
        for i in range(n):
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                index = look_up.get(target, -1)
                if index > j:
                    candidate = (nums[i], nums[j], target)
                    if candidate not in ans:
                        ret.append([nums[i], nums[j], target])
                        ans.add((nums[i], nums[j], target))
        return ret

nums =[-1,0,1,2,-1,-4]
test = Solution()
print(test.threeSum(nums))


