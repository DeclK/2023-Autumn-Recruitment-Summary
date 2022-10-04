from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_point(nums: List[int]):
            begin, end = 0, len(nums) - 1
            # 边界处理(没有旋转的情况)，否则目标超出搜索范围
            if nums[begin] < nums[-1]:
                return 0
            while begin <= end:
                mid = (begin + end) // 2
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    return mid + 1
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    return mid
                # 判断在哪一边
                if nums[mid] > nums[0]:
                    begin = mid + 1
                elif nums[mid] < nums[0]:
                    end = mid - 1
                else:
                # 如果 begin 仍然在左侧
                    if nums[begin] >= nums[0]:
                        begin += 1
                # 如果 begin 在右侧
                    else:
                        return begin
            # 只有一个数的情况
            return 0
        return nums[find_point(nums)]

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 将中值与 right 值比较
        # 如果比其大，说明中值在左侧
        # 比其小，说明中值在右侧
        # 如果相等，不知道在哪一侧，right 值 - 1
        # 让 low 卡到目标点
        # 与二分查找不同的是，不是判断 mid 是否为目标
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]
        
nums = [3,3,3,1]
nums = [10,1,10,10,10]
test = Solution()
print(test.findMin(nums))