# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # make index and node in the same dict
        if not head: return
        counter = 0
        pointer = head
        mapping = {}
        new_nodes = []
        while pointer:
            new_nodes.append(Node(pointer.val))
            mapping[id(pointer)] = counter
            pointer = pointer.next
            counter += 1
        pointer = head
        n = len(new_nodes)
        for idx in range(n):
            rand = pointer.random
            index = mapping[id(rand)] if rand else None
            new_nodes[idx].next = new_nodes[idx + 1] if idx + 1 < n else None
            new_nodes[idx].random = new_nodes[index] if rand else None

            pointer = pointer.next
        return new_nodes[0]