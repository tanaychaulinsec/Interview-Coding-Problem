import heapq
class MedianFinder:

    heaps = [], []

    def addNum(self, num):

        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
MedianFinder().addNum(1)
MedianFinder().addNum(2)
MedianFinder().addNum(3)
print(MedianFinder().findMedian())