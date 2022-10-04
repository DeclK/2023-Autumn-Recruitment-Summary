from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        target = sorted(nums)
        n = len(target)
        start = -1
        end = n
        for i in range(n):
            if nums[i] != target[i]:
                if start == -1:
                    start = i
                end = i
        return end - start + 1 if start != -1 else 0


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 尝试单调栈，双向
        s = []
        store = []
        n = len(nums)
        for idx, i in enumerate(nums):
            while s and s[-1][0] > i:
                store.append(s.pop()[1])
            s.append((i, idx))
        if store:
            left = min(store) 
        else: return 0
        store = []

        for idx, i in enumerate(nums[::-1]):
            while s and s[-1][0] < i:
                store.append(s.pop()[1])
            s.append((i, idx))
        right = n - min(store) - 1
        return right - left + 1


test = Solution()
nums = [2,6,4,8,10,9,15]
nums = [1, 2, 3]
print(test.findUnsortedSubarray(nums))

