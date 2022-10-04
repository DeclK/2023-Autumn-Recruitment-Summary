# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 使用哈希表进行查询
        pointer = head
        d = {}
        while pointer != None:
            d[pointer] = Node(pointer.val)
            pointer = pointer.next
        pointer = head
        while pointer != None:
            # 读取该 pointer.next & random 指向的 Node，并将该 Node 与其他连接
            if pointer.next:
                d[pointer].next = d[pointer.next]
            if pointer.random:
                d[pointer].random = d[pointer.random]
            pointer = pointer.next
        return d[head]