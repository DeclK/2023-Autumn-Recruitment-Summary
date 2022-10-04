from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_point(nums: List[int]):
            begin, end = 0, len(nums)
            # 确保搜索前提
            if nums[begin] <= nums[-1]:
                return -1
            while True:
                mid = (begin + end) // 2
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    return mid
                elif end - begin == 1:
                    return begin
                else:
                    if nums[mid] > nums[begin]:
                        begin = mid
                    else:
                        end = mid
        
        def find_point(nums: List[int]):
            begin, end = 0, len(nums) - 1
            # 边界处理，否则目标超出搜索范围
            if nums[begin] < nums[-1]:
                return -1
            while begin <= end:
                mid = (begin + end) // 2
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    return mid
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    return mid - 1
                if nums[mid] >= nums[begin]:
                    begin = mid + 1
                else:
                    end = mid - 1
            # 只有一个数的情况
            return -1
        return nums[find_point(nums) + 1]
        
nums = [6, 6, 1, 1, 3, 4 ,4, 5]
nums = [6,6,6,6,6,3,4]
test = Solution()
print(test.findMin(nums))