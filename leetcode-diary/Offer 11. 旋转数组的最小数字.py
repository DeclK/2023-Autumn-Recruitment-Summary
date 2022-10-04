from typing import List


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

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] < numbers[right]:
                return numbers[left]
            mid = (left + right) // 2
            if numbers[mid] < numbers[left]:
                right = mid
            elif numbers[mid] > numbers[left]:
                left = mid + 1
            else:
                left += 1
        return numbers[left]