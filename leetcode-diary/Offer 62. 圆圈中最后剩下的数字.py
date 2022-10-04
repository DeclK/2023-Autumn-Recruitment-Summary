from re import sub


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 超时了
        l = [i for i in range(n)]
        s = set(l)
        index = 0
        while len(l) > 1:
            # for i in range()
            index = (index + m - 1) % len(l)
            l.pop(index)
        return l[0]

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 尝试递归，既然删除很麻烦，那就新建更快
        def last(n, m):
            # 返回胜利者在哪一个序号
            if n == 1: return 0
            return (m + last(n - 1, m)) % n
        num = last(n, m)
        return num

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 既然递归能做，那么迭代也能做
        # 恰好这一题的递归比较简单，可以很轻松看明白
        win_index = 0
        for i in range(2, n + 1):
            win_index = (m + win_index) % i
        return win_index


test = Solution()
n = 10
m = 17
print(test.lastRemaining(n, m))