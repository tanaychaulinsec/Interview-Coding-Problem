def canJump( nums):
    maxjump=nums[0]
    for i in range(1,len(nums)):
        if maxjump==0:
            return False
        maxjump-=1
        maxjump=max(maxjump,nums[i])
        if maxjump+i>=len(nums):
            return  True
    return  True
nums=[3,2,1,0,3]
print(canJump(nums))