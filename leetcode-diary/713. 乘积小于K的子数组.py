from cgi import print_directory
from io import BufferedReader
from operator import le
from turtle import left, right
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 比较明显的双指针题目
        # 双指针常常与连续/顺序有关, 并且能够通过指针移动方便更新连续数组的性质
        # 套路: 先将右指针移动, 然后进行条件判断(移动左指针), 直到满足/不满足某个条件, 进入下一次循环
        # 通常可以使用两个循环进行左右指针的移动
        # 初始条件就是加入第一个元素
        # 但这一题的双指针不太一样...某一个指针需要按照顺序移动, 另一个指针将灵活移动
        left = 0
        prod = 1
        count = 0
        for right, val in enumerate(nums):
            # 增加一个乘积
            # 循环开始为左右指针重合, 或者此时 prod < k
            prod *= val
            while prod >= k and left <= right:
                # left 移动使其变小, 直到其乘积为 1 
                prod /= nums[left]
                left += 1
            if prod < k:
                # 如果能够找到满足的 left
                count += right - left + 1
        return count

test = Solution()
nums = [10, 5, 2, 3]
k = 3
print(test.numSubarrayProductLessThanK(nums, k))
