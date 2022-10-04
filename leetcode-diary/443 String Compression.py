from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ''
        n = len(chars)
        if n == 1:
            return chars
        count = 1
        idx = 0
        last = None
        for i in range(n):
            if i != n - 1 and chars[idx + 1] == chars[idx]:
                count += 1
                last = chars.pop(idx)
            else:
                if count != 1:
                    for i in list(f'{count}'):
                        chars.insert(idx + 1, i)
                        idx += 1
                idx += 1
                count = 1
        
        return len(chars)

test = Solution()
chars = ["a","a","b","b","c","c","c"]
print(test.compress(chars))


