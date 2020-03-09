
arr=[1,5,4,7,12,11]
n=len(arr)
res=0
dp=[1 for x in range(n)]
for i in range(n):
    dp[i]=arr[i]
    for i in range(n):
        for j in range(n):
            if arr[i]>arr[j] and dp[i]<dp[j]+arr[i]:
                dp[i]=dp[j]+arr[i]
        if res<dp[i]:
            res=dp[i]


print(res)