# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 第一想到的就是使用递归
        def revk(head):
            pointer = head
            counter = 0
            while pointer:
                pointer = pointer.next
                counter += 1
            if counter < k:
                return head
            c1 = 0
            pointer = head
            # 向前走 k - 1 次, 到达第 k 个数
            while c1 < k - 1:
                pointer = pointer.next
                c1 += 1
            res = pointer.next
            # 对剩下的做 revk
            sub_rev = revk(res)
            # 剥离第 k 个数的
            pointer.next = None
            head_rev, end = rev(head)
            end.next = sub_rev
            return head_rev

        def rev(head):
            if head is None: return None, None
            if head.next is None: return head, head
            reversed, end = rev(head.next)
            end.next = head
            head.next = None
            return reversed, head
        
        ans = revk(head)
        return ans


        
        