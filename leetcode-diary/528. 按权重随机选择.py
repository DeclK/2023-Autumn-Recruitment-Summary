import bisect
from itertools import accumulate
import random
import numpy as np
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.stack = list(accumulate(w))


    def pickIndex(self) -> int:
        num = random.randint(1, self.stack[-1])
        return bisect.bisect_left(self.stack, num)


# Your Solution object will be instantiated and called as such:
w = [1, 1]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)