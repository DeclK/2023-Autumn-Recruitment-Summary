class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
        
test = Solution()
s = '1 '
print(test.isNumber(s))