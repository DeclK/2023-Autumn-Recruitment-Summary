from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 这波直接使用单调栈不太好维护，根据思路还是应该采用一个双指针/动态规划的思想
        # 知道这个点之前的最小值和这个点之后的最大值即可解题
        max_list = []
        min_list = []
        n = len(nums)
        for i in nums[::-1]:
            if len(max_list) == 0:
                max_list.append(i)
            else:
                max_list.append(max(max_list[-1], i))
        for i in nums:
            if len(min_list) == 0:
                min_list.append(i)
            else:
                min_list.append(min(min_list[-1], i))
        max_list = max_list[::-1]
        for idx, i in enumerate(nums):
            if idx != 0 and idx != n - 1:
                if min_list[idx] < i and max_list[idx] > i:
                    return True
        return False


test = Solution()
nums =  [2,1,5,0,4,6]
print(test.increasingTriplet(nums))
