class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度搜索
        def mysum(num):
            ret = 0
            while num > 0:
                ret += num % 10
                num = num // 10
            return ret

        def is_valid(i, j, k):
            if 0 <= i < m and 0 <= j < n:
                if status[i][j] == 0 and mysum(i) + mysum(j) <= k:
                    return True
            return False

        def dfs(i, j, status):
            nonlocal count
            if is_valid(i, j, k) == False:
                return
            status[i][j] = 1
            count += 1
            search_list = [[i + 1, j], [i, j + 1]]  # 只需要向右向下遍历即可
            for i_, j_ in search_list:
                dfs(i_, j_, status)
        status = [[0] * n for i in range(m)]
        count = 0
        dfs(0, 0, status)
        return count
                
                


test = Solution()
m = 3
n = 2
k = 1
print(test.movingCount(m, n, k))