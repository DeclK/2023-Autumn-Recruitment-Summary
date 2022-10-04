# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 首先使用一个空节点头, 来处理开头
        if not head: return 
        empty = ListNode(-1)
        empty.next = head
        pointer = head
        slow_pointer = head
        previous = empty
        count = n
        while pointer.next is not None:
            count -= 1
            pointer = pointer.next
            if count <= 0:
                slow_pointer = slow_pointer.next
                previous = previous.next
        previous.next = slow_pointer.next
        return empty.next

test = Solution()
head = ListNode(1, ListNode(2, ListNode(3)))
print(test.removeNthFromEnd(head, 1))