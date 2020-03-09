T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    while start < N:
        print(*reversed(arr[start:start+K]),end=' ')
        start += K
    print()