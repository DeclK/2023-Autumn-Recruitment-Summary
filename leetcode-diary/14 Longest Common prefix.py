from typing import SupportsAbs


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        first = strs[0]
        for idx, f_str in enumerate(first):
            match = True
            for str in strs:
                if idx >= len(str) or str[idx] != f_str:
                    match = False
                    break
            if not match:
                break
            res += f_str
        return res
                
strs = ["flower","flow","flight"]
s = Solution()
print(s.longestCommonPrefix(strs))