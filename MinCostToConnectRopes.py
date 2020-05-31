import heapq
def minCostToConnectRopes(ropes):
    if not ropes and len(ropes):
        return 0
    heapq.heapify(ropes)
    cost=0
    while ropes:
        a,b=heapq.heappop(ropes),heapq.heappop(ropes)
        cost+=a+b
        if ropes:
            heapq.heappush(ropes,a+b)
    return cost

ropes=[8,4,6,12]
print(minCostToConnectRopes(ropes))

