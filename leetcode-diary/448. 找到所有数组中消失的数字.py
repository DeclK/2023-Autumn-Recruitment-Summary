from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        n = len(nums)
        for idx in range(n):
            num = nums[idx]
            while idx + 1 != num:
                # switch idx_num to num - 1 position
                if nums[num - 1] == nums[idx]:
                    break
                nums[num - 1], nums[idx] =\
                nums[idx], nums[num - 1]
                num = nums[idx]
        for i in range(n):
            if i != nums[i] - 1:
                ret.append(i + 1)
        return ret

test = Solution()
nums = [4,3,2,7,2,2,3,1]
print(test.findDisappearedNumbers(nums))