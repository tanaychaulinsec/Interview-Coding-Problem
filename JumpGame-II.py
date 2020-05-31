def minimumJump(nums):
    far=maxJump=jumpCount=0
    for i in range(len(nums)):
        maxJump=max(maxJump,nums[i]+i)

        if far<=i and i<len(nums)-1:
            far=maxJump
            jumpCount+=1
            if maxJump>=len(nums):
                return jumpCount
    return jumpCount
nums=[2,9,3,1,4,2,1,1,1,8,1]
print(minimumJump(nums))
