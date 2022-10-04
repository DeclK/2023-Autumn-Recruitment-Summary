# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 不优雅的解法
        d = {}
        pointer = headA
        while pointer != None:
            d[pointer] = 1
            pointer = pointer.next
        pointer = headB
        while pointer != None:
            if d[pointer]:
                return pointer
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 优雅永不过时
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A