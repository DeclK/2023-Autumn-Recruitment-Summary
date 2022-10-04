class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num_list = list(str(n))[::-1]
        def find_maxer(i):
            for pos in range(i):
                if num_list[pos] > num_list[i]:
                    return pos
            return None
        def switch(i, maxer):
            tempt = num_list[maxer]
            num_list[maxer] = num_list[i]
            num_list[i] = tempt
        for i in range(1, len(num_list)):
            if num_list[i] < num_list[i - 1]:
                maxer = find_maxer(i)
                switch(i, maxer)
                sort = sorted(num_list[:i], reverse=True)
                new_num = sort + num_list[i:]
                new_num = int(''.join(new_num[::-1]))
                if new_num > (2 ** 31 - 1):
                    return -1
                else:
                    return new_num
        return -1

test =Solution()
n = 230241
print(test.nextGreaterElement(n))