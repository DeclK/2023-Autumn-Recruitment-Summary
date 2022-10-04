class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        while x > 0 and y > 0:
            cur_x = x & 1
            cur_y = y & 1
            ret += cur_x ^ cur_y
            x = x >> 1
            y = y >> 1
        return ret
