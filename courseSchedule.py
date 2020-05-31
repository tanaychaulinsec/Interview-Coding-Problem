class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for _ in range(numCourses)]
        for c1,c2 in prerequisites:adjList[c2].append(c1)
        visited = set()
        stack=[]
        def hasCycle(v):
            if v in visited:
                if v in stack:
                    return True
                return False
            visited.add(v)
            stack.append(v)

            for i in adjList[v]:
                if hasCycle(i):
                    return True
            stack.pop()
            return False
        for v in range(numCourses):
            if hasCycle(v):
                return False
        return True
    # def canFinish(self, n, prerequisites):
    #     adjList = [[] for i in range(n)]
    #     degree = [0] * n
    #     for j, i in prerequisites:
    #         adjList[i]=[j]
    #         degree[j] += 1
    #     for i in range(n) :
    #         if degree[i] == 0:
    #             bfs=[i]
    #     for i in bfs:
    #         for j in adjList[i]:
    #             degree[j] -= 1
    #             if degree[j] == 0:
    #                 bfs.append(j)
    #     return len(bfs) == n


prerequisites=[[0,1],[1,0]]
numberOfCourse=2
print(Solution().canFinish(numberOfCourse,prerequisites))