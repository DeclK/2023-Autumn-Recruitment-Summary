from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 单调栈典型，找最先下降的点
        flag = False
        n = len(nums)
        for idx in range(n):
            if idx == 0: continue
            cur_idx = n - idx - 1
            if nums[cur_idx] >= nums[cur_idx + 1]:
                continue 
            else:
                flag = True
                next_idx = cur_idx + 1
                # find minimum maximum
                while next_idx < n and nums[cur_idx] < nums[next_idx]:
                    next_idx += 1
                swtich_idx = next_idx - 1
                nums[cur_idx], nums[swtich_idx] = nums[swtich_idx], nums[cur_idx]
                nums[cur_idx + 1:] = sorted(nums[cur_idx + 1:])
                break
        if not flag:
            nums[:] = nums[::-1]

test = Solution()
nums = [1,3,2]
test.nextPermutation(nums)
print(nums)