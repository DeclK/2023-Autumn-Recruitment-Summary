# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        len = 0
        pointer = head
        while pointer.next != None:
            pointer = pointer.next
            len += 1
        middile = len // 2 + 1
        pointer = head
        for i in range(middile):
            pointer = pointer.next
        return pointer

