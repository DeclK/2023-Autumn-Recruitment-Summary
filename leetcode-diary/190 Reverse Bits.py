class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            # 获得第 i 位置的数
            if n & (1 << i):
                ret = ret | (1 << (31 - i))
        return ret

n = 0b00000010100101000001111010011100
print(int(n))
test = Solution()
print(bin(test.reverseBits(n)))
print(test.reverseBits(n))