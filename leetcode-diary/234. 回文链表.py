# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        pointer = head
        while pointer:
            l.append(pointer.val)
            pointer = pointer.next
        return l == l[::-1]