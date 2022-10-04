# Definition for singly-linked list.
from re import L
from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pointer = head
        if head.val == val:
            return head.next
        next = pointer.next
        while next != None:
            if val == next.val:
                pointer.next = next.next
                break
            pointer = pointer.next
            next = next.next
        return head

test = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
val = 0
print(test.deleteNode(head, val))