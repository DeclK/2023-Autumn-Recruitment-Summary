class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counter_r = Counter(ransomNote)
        counter_m = Counter(magazine)
        flag = True
        for s, num in counter_r.items():
            if counter_m.get(s, -1) < num:
                flag = False
                break
        return flag


ransomNote = "aca"
magazine = "aab"
test = Solution()
print(test.canConstruct(ransomNote, magazine))