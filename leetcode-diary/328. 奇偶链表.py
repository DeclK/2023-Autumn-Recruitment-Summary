# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        oddhead = head
        evenhead_copy =head.next
        evenhead = head.next
        while evenhead and evenhead.next:
            oddhead.next = evenhead.next
            oddhead = evenhead.next
            evenhead.next = oddhead.next
            evenhead = oddhead.next
        oddhead.next = evenhead_copy
        return head

            