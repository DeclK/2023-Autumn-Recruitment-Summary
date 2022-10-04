from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        search_dict = {s: i for i, s in enumerate(words)}
        # 要用长的去找短的，这样才行
        def is_pa(s):
            return True if s == s[::-1] else False
        
        def find(s):
            return search_dict.get(s, -1)

        ret = []
        for idx, word in enumerate(words):
            m = len(word)
            for i in range(m + 1):
                prefix = word[:i]
                post = word[i:]
                if is_pa(prefix):
                    res = word[i:][::-1]
                    search_id = find(res)
                    if search_id != -1 and search_id != idx:
                        ret.append([search_id, idx])
                if i != m and is_pa(post):  # 当全部算入时，寻找的都是长度相等的字符串，所以一定会被重复计算，故只能算一次
                    res = word[:i][::-1]
                    search_id = find(res)
                    if search_id != -1 and search_id != idx:
                        ret.append([idx, search_id])
        return ret

test = Solution()
words = ["abcd","dcba","lls","s","sssll"]
words = ['a', '']
print(test.palindromePairs(words))