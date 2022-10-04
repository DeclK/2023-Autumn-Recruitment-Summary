class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')
        ret = None
        print(l)
        for word in l[::-1]:
            if word != '':
                ret = word
                break
        print(ret)
        return len(ret)

# s = "   fly me   to   the moon  "
# test = Solution()
# print(test.lengthOfLastWord(s))