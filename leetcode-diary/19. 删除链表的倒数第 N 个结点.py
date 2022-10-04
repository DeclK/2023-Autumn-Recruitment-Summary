# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return
        def getlength(head):
            pointer = head
            counter = 0
            while pointer:
                pointer = pointer.next
                counter += 1
            return counter
        m = getlength(head)
        k = m - n
        counter = 0
        empty = ListNode()
        empty.next= head
        pointer_pre = empty
        pointer = head
        while counter < k:
            pointer = pointer.next
            pointer_pre = pointer_pre.next
            counter += 1
        pointer_pre.next = pointer.next
        return empty.next
