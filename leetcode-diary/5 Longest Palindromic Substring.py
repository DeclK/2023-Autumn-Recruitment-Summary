class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 其实一个 n^2 的方法也还不错，当想不到其他好方法时应当尽快尝试
        # 对所有的中心进行扩散
        n = len(s)
        def search(i):
            if i % 2 == 0:
                i = i // 2
                left = i - 1
                right = i + 1
            else:
                i = i // 2
                left = i
                right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left, right = left - 1, right + 1
                else:
                    break
            return s[left + 1:right]
        center = 2 * n - 1
        ans = ''
        for i in range(center):
            sub_ans = search(i)
            if len(sub_ans) > len(ans):
                ans = sub_ans
        return ans

test = Solution()
s = "cbabd"
print(test.longestPalindrome(s))