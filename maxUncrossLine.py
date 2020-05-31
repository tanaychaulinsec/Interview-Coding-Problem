def maxUncrossedLines(A, B):
    m, n = len(A), len(B)
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n-1,-1,-1):
            if A[i] == B[j]:
                dp[j + 1] = dp[j] + 1
        for j in range(n):
            dp[j + 1] = max(dp[j + 1], dp[j])
    return dp[n]

A=[2,5,1,2,5]
B=[10,5,2,1,5,2]
print(maxUncrossedLines(A,B))