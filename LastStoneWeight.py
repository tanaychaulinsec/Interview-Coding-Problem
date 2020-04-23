import heapq
def lastStoneWeight(stones):
    stones = [-n for n in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y, x = heapq.heappop(stones), heapq.heappop(stones)
        if y < x:
            heapq.heappush(stones, y-x)
    return -stones[0] if stones else 0
stones=[2,7,4,1,8,1]
print(lastStoneWeight(stones))