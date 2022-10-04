# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursion
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        pointer = node = ListNode()
        pointer.val = l1.val + l2.val
        sub_l = self.addTwoNumbers(l1.next, l2.next)
        pointer.next = sub_l
        while pointer.val >= 10:
            res = pointer.val % 10
            pointer.val = res
            if pointer.next is None:
                pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = pointer.val + 1
        return node

l1= ListNode(2)
l2 = ListNode(8)
test = Solution()
print(test.addTwoNumbers(l1, l2).next.val)