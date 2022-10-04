# Definition for singly-linked list.
from typing import _get_type_hints_obj_allowed_types


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = self.get_list(headA)[::-1]
        l2 = self.get_list(headB)[::-1]
        if l1[0] is not l2[0]:
            return None
        for i in range(len(l1)):
            if i < len(l2) and l1[i] is not l2[i]:
                return l1[i-1]
            else:
                return  l1[i]
        return l1[-1]


    def get_list(self, head):
        l = []
        pointer = head
        while pointer != None:
            l.append(pointer)
            pointer = pointer.next
        return l