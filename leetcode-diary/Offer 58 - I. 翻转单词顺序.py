class Solution:
    def reverseWords(self, s: str) -> str:
        # 不使用字符串方法来完成一次
        ans = []
        word = ''
        for i in s:
            if i != ' ':
                word += i
            if i == ' ' and word != '':
                ans.append(word)
                word = ''
        if word != '': ans.append(word)
        return ' '.join(ans[::-1])

test = Solution()
s = "the sky is blue"
print(test.reverseWords(s))
