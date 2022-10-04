from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []
        for word in words:
            for word_ in words:
                if word_ != word and word in word_:
                    ret.append(word)
                    break
        return ret