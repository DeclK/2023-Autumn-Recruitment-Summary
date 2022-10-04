from typing import List
import time

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        def expand(idx, num):
            if idx % 2 == 0:
                return [num << 1, (num << 1) + 1]
            else:
                return [(num << 1) + 1, num << 1]
        sub = self.grayCode(n - 1)
        ret = []
        for i in range(len(sub)):
            ret += expand(i, sub[i])
        return ret

        
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        sub = self.grayCode(n - 1)
        rev = [num + (1<<(n-1)) for num in sub[::-1]]
        return sub + rev

test = Solution()
n = 20
print(test.grayCode(n)) 