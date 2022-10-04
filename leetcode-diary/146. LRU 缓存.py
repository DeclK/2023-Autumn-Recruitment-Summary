from collections import deque


class LRUCache:
# use deque
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.priority = deque() # left is new, right is old
                                # deque is a approximation for double link list
    def get(self, key: int) -> int:
        ret = self.d.get(key, -1)
        if ret != -1:
            # update priority
            self.priority.remove(key)
            self.priority.appendleft(key)
        return ret

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        if key in self.priority:
            self.priority.remove(key)
        self.priority.appendleft(key)
        # update priority and dict
        if self.capacity < len(self.d):
            key = self.priority.pop()
            self.d.pop(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

test = LRUCache(2)
test.put(1,1)
test.put(2,2)
test.get(1)
test.put(3,3)
test.get(2)
test.put(4,4)
test.get(1)
test.get(3)
test.get(4)