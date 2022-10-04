from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 直接先看最小最大值，然后再看其他
        non_zero = [i for i in nums if i != 0]
        if len(non_zero) != len(set(non_zero)): return False
        mini, maxi = min(non_zero), max(non_zero)
        if mini + 4 <= maxi: return True
        else: return False