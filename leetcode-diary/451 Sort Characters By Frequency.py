class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s).most_common()
        ret = ''
        for s_, nums in counter:
            ret += s_ * nums
        return ret


test = Solution()
print(test.frequencySort('treeersrgcs'))