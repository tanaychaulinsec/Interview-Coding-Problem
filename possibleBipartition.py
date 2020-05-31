from collections import defaultdict
def possibleBipartition( N, dislikes) -> bool:
    graph = defaultdict(list)
    a=1^1
    b=0^1
    c=2^1
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    color = [-1] * (N + 1)
    for i in range(1, N + 1):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                node = stack.pop()
                for j in graph[node]:
                    if color[j] == color[node]:
                        return False
                    if color[j] == -1:
                        color[j] = color[node] ^ 1
                        stack.append(j)
    return True

dislikes=[[1,2],[1,3],[2,4]]
N=4
print(possibleBipartition(N,dislikes))