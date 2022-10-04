# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = {}
        pointer = head
        counter = 0
        while pointer:
            if pointer not in d:
                d[pointer] = counter
            else:
                return d[pointer]
            pointer = pointer.next
            counter += 1
        return -1