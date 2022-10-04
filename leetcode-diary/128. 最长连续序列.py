from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 先实现暴力版本, 通过为第一奥义
        nums = sorted(set(nums))
        ans = 1
        sub = 1
        n = len(nums)
        if n == 0: return 0
        for i in range(n - 1):
            if nums[i] == nums[i + 1] - 1:
                sub += 1
            else:
                ans = max(ans, sub)
                sub = 1
        ans = max(ans, sub)
        return ans

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 比较自然地就想到了连通的思想
        # 如果每一个数都记录了自己的左右邻居是否存在即可
        num_set = set(nums)
        def find_neighbor(x):
            ret = 0
            nonlocal num_set
            neighbor = [x - 1, x + 1]
            if neighbor:
                left = neighbor[0]
                while left in num_set:
                    num_set.discard(left)
                    left -= 1
                    ret += 1
                right = neighbor[1]
                while right in num_set:
                    num_set.discard(right)
                    right += 1
                    ret += 1
            return ret
        ans = 0
        while num_set:
            num = num_set.pop()
            neighbor_num = find_neighbor(num) + 1
            ans = max(ans, neighbor_num)
        return ans
            


test = Solution()
nums = nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [100,4,200,1,3,2]
print(test.longestConsecutive(nums))