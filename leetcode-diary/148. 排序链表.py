# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brutal
        l = []
        pointer = head
        while pointer:
            l.append(pointer)
            pointer = pointer.next
        l = sorted(l, key=lambda x: x.val)
        n = len(l)
        for idx in range(n):
            if idx == n - 1:
                l[idx].next = None
                continue
            l[idx].next = l[idx + 1]
        return l[0]


def quick_sort(array):
    def partition(start, end):
        check = array[start]
        anchor = start + 1
        for i in range(start + 1, end + 1):
            if array[i] < check:
                array[anchor], array[i] = array[i], array[anchor]
                anchor += 1
        array[start], array[anchor - 1] = array[anchor - 1], array[start]
        return anchor - 1
    def q_sort(start, end):
        if start >= end: return
        anchor = partition(start, end)
        q_sort(start, anchor - 1)
        q_sort(anchor + 1, end)
    n = len(array)
    return q_sort(0, n-1)

test = [402, 1, 3, -1, 32, 2, 43]
print(quick_sort(test), test)