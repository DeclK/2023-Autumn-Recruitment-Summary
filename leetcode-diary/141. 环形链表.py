# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if fast: fast = fast.next
            else: return False
            slow = slow.next
            if fast == slow: return True
        return False