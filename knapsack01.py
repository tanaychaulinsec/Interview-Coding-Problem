def maxValue(wt,profit,capacity):
    n=len(wt)
    dp=[[0 for x in range(capacity+1)] for y in range(n+1)]
    for row in range(n+1):
        for column in range(capacity+1):
            if row==0 or column==0:
                dp[row][column]=0
            elif wt[row-1]<=column:
                dp[row][column]=max(profit[row-1]+dp[row-1][column-wt[row-1]],dp[row-1][column])
            else:
                dp[row][column]=dp[row-1][column]
    return dp[row][column]

wt=[1,2,3,5]
profit=[1,6,10,16]
capacity=7
print(maxValue(wt,profit,capacity))