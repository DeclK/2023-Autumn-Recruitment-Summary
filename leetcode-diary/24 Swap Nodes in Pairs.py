# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # recursive idea
        pointer_1 = head
        if pointer_1 == None or pointer_1.next == None:
            return pointer_1
        # original pointer
        pointer_2 = pointer_1.next
        pointer_3 = pointer_2.next
        
        pointer_1 = pointer_2
        pointer_1.next = head
        pointer_1.next.next = self.swapPairs(pointer_3)
        return pointer_1

l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
test  = Solution()
print(test.swapPairs(l))