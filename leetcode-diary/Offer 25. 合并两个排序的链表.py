# Definition for singly-linked list.
from tempfile import template


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:  return l2
        if l2 == None:  return l1
        val1 = l1.val
        val2 = l2.val
        if val1 > val2:
            head = l2
            sub_ans = self.mergeTwoLists(l1, l2.next)
        else:
            head = l1
            sub_ans = self.mergeTwoLists(l1.next, l2)
        head.next = sub_ans
        return head

# 非递归解法，使用一个空节点来作为头部，以便于处理初始情况
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dum = ListNode(None)
        pointer = dum
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            if val1 > val2:
                pointer.next = l2
                l2 =l2.next
            else:
                pointer.next = l1
                l1 = l1.next
            pointer = pointer.next
        pointer.next = l1 if l1 else l2
        return dum.next

