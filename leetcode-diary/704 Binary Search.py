
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        # 终止条件
        while begin <= end:
            # 二分
            mid = (begin + end) // 2
            # 判断是否正确
            if nums[mid] == target:
                return mid
            # 更改搜索范围
            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    begin = mid + 1
        return -1

test = Solution()
print(test.search([1, 2], 2))