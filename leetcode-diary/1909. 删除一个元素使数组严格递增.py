from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        if n == 1: return True
        count = 0
        for i in range(n):
            if i == 0: stack.append(nums[i])
            elif nums[i] <= stack[-1]:
                if i == 1:
                    stack.pop()
                    stack.append(nums[i])
                if nums[i] > nums[i - 2]:
                    stack.pop()
                    stack.append(nums[i])
                count += 1
            else:
                stack.append(nums[i])
        if count <= 1: return True
        return False

test = Solution()
nums = [1,2,10,5,7]
print(test.canBeIncreasing(nums))
