# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        pointer = head
        while pointer != None:
            stack.insert(pointer.val, 0)
            pointer = pointer.next
        return stack