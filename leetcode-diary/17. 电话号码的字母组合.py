from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(map(int, list(digits)))
        letter_map = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }
        for k, v in letter_map.items():
            letter_map[k] = list(v)
        candidiate = []
        for digit in digits:
            candidiate.append(letter_map[digit])
        ans = []
        for candi in candidiate:
            if not ans:
                ans = candi
            else:
                new_ans = []
                for candi_str in ans:
                    for new_str in candi:
                        new_ans.append(candi_str + new_str)
                ans = new_ans
        return ans

digits = '23'
test = Solution()
print(test.letterCombinations(digits))