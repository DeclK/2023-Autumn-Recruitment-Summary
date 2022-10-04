from operator import le
from typing import List
from unicodedata import numeric


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 不使用额外空间，可以使用双指针不断比较两个数
        # 若左指针为偶数，右指针为奇数，则交换
        # 若左指针为偶数，右指针为偶数，则右指针移动
        # 若左指针为奇数，右指针为偶数，则共同移动
        # 若左指针为奇数，右指针为奇数，则左指针移动
        left = 0
        right =len(nums) - 1
        while left < right:
            if nums[right] % 2 == 0:
                right -= 1
            if nums[left] % 2 != 0:
                left += 1
            elif nums[right] % 2 != 0:
                tempt = nums[left]
                nums[left] = nums[right]
                nums[right] = tempt
        return nums

test = Solution()
nums = [11,9,3,7,16,4,2,0]
print(test.exchange(nums))