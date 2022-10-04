from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        num = target // 2 + 1
        ans = []
        stack = []
        summ = 0
        for i in range(1, num + 1):
            stack.append(i)
            summ += i
            if summ == target: ans.append(stack[:])
            elif summ > target:
                while stack and summ > target:
                    summ = summ - stack.pop(0)
                    if summ == target: ans.append(stack[:])
        return ans

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 公式法
        num = target // 2 + 1
        ans = []
        for i in range(1, num + 1):
            delta = 1 + 4 * (2 * target  + i ** 2 - i)
            res = int(delta ** 0.5)
            if res ** 2 == delta:
                j = (res - 1) % 2
                if j == 0:  
                    j = (res - 1) // 2
                    ans.append([k for k in range(i, j + 1)])
        return ans


test = Solution()
target = 15
print(test.findContinuousSequence(target))