from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums1 = [str(i) for i in nums1]
        nums2 = [str(i) for i in nums2]

        def get_set(num: list, k):
            # 留下 k 个
            n = len(num)
            if n <= k: return ''.join(num)
            stack = []
            count = 0
            for i in range(n):
                while count < n - k and stack and num[i] > stack[-1]:
                    stack.pop()
                    count += 1
                stack.append(num[i])
            return ''.join(stack)[:k]
        
        def combine(num1: str, num2: str):
            ret = ''
            while num1 or num2:
                if num1 > num2:
                    ret += num1[0]
                    num1 = num1[1:]
                else:
                    ret += num2[0]
                    num2 = num2[1:]
            return ret
        ans = 0
        for i in range(k + 1):
            sub_1 = get_set(nums1, i)
            sub_2 = get_set(nums2, k - i)
            sub_ans = combine(sub_1, sub_2)
            ans = max(ans, int(sub_ans))
        ans = [int(i) for i in list(str(ans))]
        return ans
        

test = Solution()
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print(test.maxNumber(nums1, nums2, k))