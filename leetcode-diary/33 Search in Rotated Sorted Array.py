from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_point(nums: List[int]):
            begin, end = 0, len(nums) - 1
            if nums[begin] < nums[-1]:
                return end
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
            return -1
        def searchInsert(nums: List[int], target: int) -> int:
                begin, end = 0, len(nums) - 1
                while begin <= end:
                    mid = (end + begin) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        end = mid - 1
                    else:
                        begin = mid + 1
                return -1e5
        point = find_point(nums) + 1
        idx = max(searchInsert(nums[:point], target), searchInsert(nums[point:], target) + point, -1)
        return idx
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                # 均在左
                if target >= nums[0]:
                    if target > nums[mid]:
                        begin = mid + 1
                    else:
                        end = mid - 1
                # mid 在左，target 在右
                else:
                    begin = mid + 1
            else:
                # mid 在右，target 在左
                if target >= nums[0]:
                    end = mid - 1
                # 均在右
                else:
                    if target > nums[mid]:
                        begin = mid + 1
                    else:
                        end = mid - 1


nums = [4,5,6,7,0,1,2]
target = 3
test = Solution()
print(test.search(nums, target))
