# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 尝试原地修改链表
        pointer = head
        nextp = pointer.next
        pointer.next = None
        while nextp != None:
            tempt = nextp.next
            nextp.next = pointer
            pointer = nextp
            nextp = tempt
        return pointer


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 尝试递归
        def recur(head):
            if head == None:
                return None, None
            if head.next == None:
                return head, head
            rev_head, end = recur(head.next)
            end.next = head
            head.next = None
            return rev_head, head
        return recur(head)[0]

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 重新写一遍反转链表
        if head is None: return None
        if head.next is None:
            return head
        reversed = self.reverseList(head.next)
        pointer = reversed
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = head
        head.next = None
        return reversed

test = Solution()
head =ListNode(1, ListNode(2))
print(test.reverseList(head))