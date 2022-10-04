from turtle import left, right
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import bisect
        index = bisect.bisect_left(arr, x)
        # 需要讨论 x 是否在 arr 中
        flag = x in arr
        if flag:
            left = index - 1
            right = index + 1
            k = k - 1
        else:
            left = index - 1
            right = index
        
        def check(idx):
            return 0 <= idx < len(arr)
        for _ in range(k):
            if check(left) and check(right):
                l_dist = (abs(arr[left] - x), arr[left])
                r_dist = (abs(arr[right] - x), arr[right])
                if l_dist < r_dist:
                    left -= 1
                else:
                    right += 1
            elif check(left):
                left -= 1
            elif check(right):
                right += 1
        return arr[left + 1: right]

test = Solution()
arr =[0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
print(test.findClosestElements(arr, k, x))
