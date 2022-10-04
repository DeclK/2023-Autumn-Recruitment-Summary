class Solution(object):
    def removeElement(self, nums: list, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        for i in nums:
            if i != val:
                nums[counter] = i
                counter += 1
        return counter

# 但实际测试来看，remove 操作耗时是相同的
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break
        return len(nums) 

nums = [0,1,2,2,3,0,4,2]
val = 2
test = Solution()
print(test.removeElement(nums, val))