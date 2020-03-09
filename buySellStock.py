def buySellStock(prices):
    minP=float('inf')
    res=0
    for p in prices:
        minP=min(minP,p)
        res=max(res,p-minP)
    return res

prices=[7,1,3,9,5,6,8]
print(buySellStock(prices))