import heapq
def klargest(K,nums):
    heapq.heapify(nums)
    return heapq.nlargest(K,nums)

T=int(input())
for i in range(T):
    N,K=list(map(int,input().split()))
    nums=list(map(int,input().split()[:N]))
    print(klargest(K,nums))