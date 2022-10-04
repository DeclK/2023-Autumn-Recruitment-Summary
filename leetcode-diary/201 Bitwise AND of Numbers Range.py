class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 逐个某个位是否会经过零，那么我们就假定这个位为0，来看看什么会发生
        # 如果这个位高于 right 则必定为0，如果低于 right，则需要看 left 决定是否能经过 0
        # 实际上将 right 这一位数字变为0，后面的数字全为 1，如果这个数字小于 left 则这一位不能经过0，反之一定能经过0
        ret = 0
        mask = 1 << 32 - 1
        for i in range(32, 0, -1):
            mask = mask >> 1
            if right < (1 << (i - 1)) or left < (1 << (i - 1)):
                continue
            if right & (1 << (i - 1)):
                tempt = right ^ (1 << (i - 1))
                tempt = tempt | mask
                if tempt < left:
                    ret += (1 << (i - 1))
        return ret


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift


left = 5
right = 6
test = Solution()
print(test.rangeBitwiseAnd(left, right))