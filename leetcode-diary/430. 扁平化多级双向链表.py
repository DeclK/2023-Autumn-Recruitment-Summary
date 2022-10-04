# Definition for a Node.

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # recurrsive
        def flatten_(head):
            # return head and tail
            if not head: return None, None
            if head.next is None and head.child is None:
                return head, head
            pointer = head
            tail = None
            while pointer:
                if pointer.child:
                    c_head, c_tail = flatten_(pointer.child)
                    pointer.child = None
                    pointer.next, c_tail.next, c_head.prev,  = c_head, pointer.next, pointer
                    pointer = c_tail
                    if pointer.next:
                        pointer.next.prev = pointer
                else:
                    if pointer.next is None:
                        tail = pointer                    
                    pointer = pointer.next

            return head, tail
        ret = flatten_(head)[0]
        return ret



node = Node(0, Node(-1), Node(1), Node(2))
test = Solution()
print(test.flatten(node))