# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sort by val
        merge_list = []
        for llist in lists:
            pointer = llist
            while pointer:
                item = (pointer.val, pointer)
                merge_list.append(item)
                pointer = pointer.next
        # rank
        merge_list = sorted(merge_list, key=lambda x: x[0])
        n = len(merge_list)
        if n == 0: return
        for i in range(n):
            if i < n - 1:
                merge_list[i][1].next = merge_list[i + 1][1]
            else:
                merge_list[i][1].next = None
        return merge_list[0][1]
            
