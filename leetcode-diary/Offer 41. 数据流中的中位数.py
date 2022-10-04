from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []


    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heappush(self.maxheap, -num)
            heappush(self.minheap, -heappop(self.maxheap))
        else:
            heappush(self.minheap, num)
            heappush(self.maxheap, -heappop(self.minheap))
    def findMedian(self) -> float:
        if self.minheap:
            if len(self.minheap) == len(self.maxheap):
                return (self.minheap[0] + self.maxheap(0)) // 2
            else: return self.minheap[0]
        else: return None



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()