def minimumJump(nums):
    far=maxJump=jumpDis=0
    for i in range(len(nums)):
        maxJump=max(maxJump,nums[i]+i)
        if far<=i and i<len(nums)-1:
            far=maxJump
            jumpDis+=1
            if maxJump>=len(nums):
                return jumpDis
    return jumpDis
nums=[2,9,3,1,4,2,1,1]
print(minimumJump(nums))
