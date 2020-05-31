def friendCircle(matrix):
    n=len(matrix)
    res=0
    def dfs(i):
        matrix[i][i]=0
        for j in range(n):
            if matrix[i][j]==1 and matrix[j][j]==1:
                dfs(j)
    for i in range(n):
        if matrix[i][i]==1:
            dfs(i)
            res+=1
    return res

matrix=[[1,1,0],[1,1,0],[0,0,1]]
print(friendCircle(matrix))
