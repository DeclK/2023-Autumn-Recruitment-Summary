class Solution:
    def sumNums(self, n: int) -> int:
        ans = 0
        def sub(n):
            nonlocal ans
            n > 1 and sub(n - 1)
            ans += n
        sub(n)
        return ans

test = Solution()
n = 3
print(test.sumNums(n))