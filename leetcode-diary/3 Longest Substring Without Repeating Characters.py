class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 首先想到双指针，因为两头都在移动
        left = 0
        right = 0
        ans = 0
        d = {}
        while right < len(s):
            if d.get(s[right]):
                d.pop(s[left])
                left += 1
            else:
                d[s[right]] = 1
                right += 1
                ans = max(ans, right - left)
        return ans

test = Solution()
s = "pwwkew"
print(test.lengthOfLongestSubstring(s))