class Solution:
    def translateNum(self, num: int) -> int:
        # 比较明显的一道搜索题
        num = str(num)
        ans = 0
        def dfs(pos):
            nonlocal ans
            if pos == len(num):
                ans += 1
                return 
            dfs(pos + 1)
            if pos + 1 < len(num) and num[pos] > '0' and num[pos] + num[pos + 1] < '26':
                dfs(pos + 2)
        dfs(0)
        return ans

test = Solution()
num = 12258
print(test.translateNum(num))