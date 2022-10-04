from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for i in strs:
            template = ''.join(sorted(i))
            d[template].append(i)
        return list(d.values())



test = Solution()
strs = ["ddddddddddg","dgggggggggg"]
print(test.groupAnagrams(strs))