def houseRobber (loot):
    if len(loot)==0 or loot==None:
        return 0
    elif len(loot)==1:
        return loot[0]
    elif len(loot)==2:
        return max(loot[0],loot[1])
    prev1=max(loot[0],loot[1])
    prev2=loot[0]
    curr=0
    for i in range(2,len(loot)):
        curr=max(prev1,prev2+loot[i])
        prev2=prev1
        prev1=curr
    return curr

loot=[2,7,9,3,1]
print(houseRobber(loot))