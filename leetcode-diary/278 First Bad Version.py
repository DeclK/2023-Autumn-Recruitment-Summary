# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        end, begin = n, 1
        while begin <= end:
            mid = (end + begin) // 2
            # 为避免多次查询，先存储结果
            result = isBadVersion(mid)
            # 考虑边界，如果找不到说明答案为 begin，因为该搜索必定有结果
            if mid > 1 and result and isBadVersion(mid - 1) == False:
                return mid
            elif result == False:
                begin = mid + 1
            else:
                end = mid - 1
        return 1