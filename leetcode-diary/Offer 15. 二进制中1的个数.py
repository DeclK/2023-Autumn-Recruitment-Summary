from itertools import count


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 方法一，偷懒大法
        # return str(bin(n)).count('1')
        # 方法二，对每一个位进行检查
        count = 0
        for i in range(32):
            check = 1 << i
            if n & check:
                count += 1
        return count

test = Solution()
n = 111
print(test.hammingWeight(n))