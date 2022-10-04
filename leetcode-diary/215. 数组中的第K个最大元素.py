from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # try again
        def partition(start, end):
            anchor = nums[start]
            pos = start + 1
            for idx in range(start + 1, end + 1):
                if nums[idx] < anchor:
                    nums[idx], nums[pos] = \
                    nums[pos], nums[idx]
                    pos += 1
            nums[start], nums[pos - 1] = \
            nums[pos - 1], nums[start]
            return pos - 1
        n = len(nums)
        self.ans = None
        def quick_sort(start, end):
            if start > end: return
            if self.ans is not None: return
            pos = partition(start, end)
            if pos == n - k:
                self.ans = nums[pos]
                return
            quick_sort(start, pos - 1)
            quick_sort(pos + 1, end)
        quick_sort(0, n - 1)
        return self.ans