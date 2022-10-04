# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        if pointer1 == None:
            return pointer2
        elif pointer2 == None:
            return pointer1
        if pointer1.val > pointer2.val:
            ret = pointer2
            pointer2.next = self.mergeTwoLists(pointer1, pointer2.next)
        else:
            ret = pointer1
            pointer1.next = self.mergeTwoLists(pointer1.next, pointer2)
        return ret
        
        # while pointer1.next != None and pointer2.next != None:
        #     if pointer1.next is None:

            # if pointer1.val > pointer2.val:
            #     tempt = pointer2
            #     pointer2.next = pointer1
            #     pointer2 = tempt
            # elif :
            #     tempt = pointer1
            #     pointer1.next = pointer2
            #     pointer2 = tempt
                