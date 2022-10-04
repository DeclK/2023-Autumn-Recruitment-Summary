# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        def getlength(head):
            counter = 0
            pointer = head
            while pointer:
                pointer = pointer.next
                counter += 1
            return counter
        n = getlength(head)
        k = k % n
        if k == 0: return head
        m = n - k
        pointer = head
        counter = 1
        while counter < m:
            pointer = pointer.next
            counter += 1
        start = pointer.next
        pointer.next = None
        pointer = start
        while pointer.next:
            pointer = pointer.next
        pointer.next = head
        return start
