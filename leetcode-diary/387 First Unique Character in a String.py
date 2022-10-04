from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        idx = -1
        for str in s:
            if counter[str] == 1:
                idx = s.index(str)
                break
        return idx

s = 'loveleetcode'
test = Solution()
print(test.firstUniqChar(s))