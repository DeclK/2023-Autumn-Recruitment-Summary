from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 在于如何充分利用已经求得的条件，并将其进行组合
        # 既然没办法进行删除，那就进行拼接
        n = len(a)
        store = [[1] * n for i in range(2)]
        for i in range(1, n):
            store[0][i] = store[0][i - 1] * a[i - 1]
        for i in range(n - 2, -1, -1):
            store[1][i] = store[1][i + 1] * a[i + 1]
        ret = [0] * n
        for i in range(n):
            ret[i] = store[0][i] * store[1][i]
        return ret

test = Solution()
a = [1, 2, 3, 4, 5]
print(test.constructArr(a))