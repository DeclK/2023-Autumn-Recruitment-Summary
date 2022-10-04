from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.maxi = []
        self.mini = []


    def addNum(self, num: int) -> None:
        if len(self.maxi) == len(self.mini):
            heappush(self.maxi, -num)
            heappush(self.mini, -heappop(self.maxi))
        else:
            heappush(self.mini, num)
            heappush(self.maxi, -heappop(self.mini))


    def findMedian(self) -> float:
        if len(self.maxi) == len(self.mini):
            return (self.mini[0] - self.maxi[0]) / 2 if self.maxi else None
        else:
            return self.mini[0] if self.mini else None

test = MedianFinder()
test.addNum(6)
print(test.findMedian())
test.addNum(10)
print(test.findMedian())
test.addNum(2)
print(test.findMedian())
test.addNum(4)
test.addNum(5)
test.addNum(6)
test.addNum(6)
# print(test.findMedian())