# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 由于链表不好往前移动，尝试用一个列表存储节点
        # 另一个方法显然就是使用双指针
        pointer = head
        count =  k
        ret = head
        while pointer != None:
            count -= 1
            if count < 0:
                ret = ret.next
            pointer = pointer.next
        return ret