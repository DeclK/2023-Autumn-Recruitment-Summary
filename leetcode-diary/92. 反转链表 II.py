# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(head):
            if head is None: return None, None
            if head.next is None: return head, head
            res = head.next
            res_head, res_tail = reverse(res)
            res_tail.next = head
            head.next = None 
            return res_head, head
        counter = 0
        start = None
        after_end = None
        empty = ListNode()
        empty.next = head
        pointer = empty
        while pointer is not None:
            if counter == left - 1:
                start = pointer.next
                before_start = pointer
            if counter == right:
                after_end = pointer.next
                pointer.next = None
            pointer = pointer.next
            counter += 1
        rev, rev_end = reverse(start)
        before_start.next = rev
        rev_end.next = after_end
        return empty.next

test = ListNode(1, ListNode(2, ListNode(3)))
s = Solution()
ans = s.reverseBetween(test, 1, 1)
print(ans)


