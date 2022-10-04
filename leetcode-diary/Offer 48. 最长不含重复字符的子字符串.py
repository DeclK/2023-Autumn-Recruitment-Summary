import collections
from operator import le


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 之前做过这题，双指针 + 哈希表存储
        left = 0
        right = 0
        n = len(s)
        ans = 0
        d = collections.defaultdict(int)
        while right < n:
            if d[s[right]] != 0:
                d[s[left]] -= 1
                left += 1
            else:
                d[s[right]] += 1
                right += 1
                ans = max(ans, right - left)
        return ans


test = Solution()
s = "pwwkebwe4c"
print(test.lengthOfLongestSubstring(s))