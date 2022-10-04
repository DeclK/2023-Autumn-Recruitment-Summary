from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict.fromkeys(nums, 0)
        counter = 0
        for i in range(len(nums)):
            if d[nums[i]] == 0:
                d[nums[i]] = 1
                nums[counter] = nums[i]
                counter += 1
            else:
                nums[counter] = nums[i]
        return counter

nums = [0,0,1,1,1,2,2,3,3,4]
val = 2
test = Solution()
print(test.removeDuplicates(nums))
print(nums)