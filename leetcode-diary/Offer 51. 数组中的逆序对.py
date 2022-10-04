from typing import List

import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:return
        l = []
        ans = 0
        for i in nums:
            index = bisect.bisect_right(l, i)
            l[index:index] = [i]
            ans += len(l) - index - 1
        return ans

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # merge sort
        def merge_sort(array):
            if len(array) <= 1: return array, 0
            mid = len(array) // 2
            l, l_ans = merge_sort(array[:mid])
            r, r_ans = merge_sort(array[mid:])
            new_array = []
            left = 0
            right = 0
            ans = l_ans + r_ans
            for i in range(len(array)):
                if left == len(l):
                    new_array.append(r[right])
                    right += 1
                elif right == len(r):
                    new_array.append(l[left])
                    left += 1
                else:
                    if l[left] > r[right]:
                        new_array.append(r[right])
                        right += 1
                        ans += len(l)- left
                    else:
                        new_array.append(l[left])
                        left += 1
            return new_array, ans
        sorted_array, ans = merge_sort(nums)
        return ans
        
test = Solution()
nums =  [7,5,6,4]
print(test.reversePairs(nums))