from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 每次都判断一下是否要 pop
        # 看最终能否 pop 完
        n = len(pushed)
        if n == 0:return True
        stack = []
        push_idx = pop_idx = 0
        while pop_idx < n:
            if stack:
                if stack[-1] == popped[pop_idx]:
                    stack.pop()
                    pop_idx += 1
                elif push_idx < n:
                    stack.append(pushed[push_idx])
                    push_idx += 1
                else:
                    pop_idx += 1
            elif push_idx < n:
                stack.append(pushed[push_idx])
                push_idx += 1
        return False if len(stack) else True

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 先入栈，然后再来看出栈
        stack = []
        for i in pushed:
            stack.append(i)
            while popped:
                if stack[-1] == popped[0]:
                    popped.pop(0)
                    stack.pop()
                else:break
        return False if len(stack) else True
        
            

test = Solution()
pushed = [1, 2, 3, 4, 5]
popped = [4,3,5,1,2]
print(test.validateStackSequences(pushed, popped))

