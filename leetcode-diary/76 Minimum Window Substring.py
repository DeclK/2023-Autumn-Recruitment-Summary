import collections
from operator import le
from turtle import left


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 放弃了动态规划过后只能够从问题的本质入手了，也就是是否丢弃一个数字
        # 还是搞双指针（队列），随着右指针的增加，左指针所指的数超越满足，那就可以丢弃
        # 需要一个函数来判断该区间是否满足
        left = right = 0
        n = len(s)
        d = collections.defaultdict(int)
        td = collections.Counter(t)
        def is_satisfied():
            # 判断左侧字符 s 是否能丢弃
            # ret = [True, True]
            for key, val in td.items():
                if val > d[key]:
                    return False
            return True
        def can_pop(left):
            if is_satisfied() and d[s[left]] > td[s[left]]:
                return True
            return False
        ans = [0 , 1e5]
        while s[left] not in td:
            left += 1
            if left > n - 1:
                return ""
        right = left
        while right < n:
            if s[right] in td:
                d[s[right]] += 1
                # 先判断整体是否满足，如果满足就计算答案
                # 如果在满足的条件下，还能 pop 左侧则继续 pop 直到不能 pop
                if is_satisfied():
                    while can_pop(left):
                        d[s[left]] -= 1
                        left += 1
                        while s[left] not in td:
                            left += 1
                    if right - left < ans[1] - ans[0]:
                        ans = [left, right]
            right += 1
        return s[ans[0]: ans[1] + 1] if is_satisfied() else ""


test = Solution()
s = "ab"
t = "a"
print(test.minWindow(s, t))