class Solution:
    def reverseWords(self, s: str) -> str:
        def is_space(s):
            if s == ' ':
                return False
            return True
        print(s.split())
        
        l = list(filter(is_space, s.split()))
        return ' '.join(l[::-1])

test = Solution()
s = "  hello world  "
print(test.reverseWords(s))