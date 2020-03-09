nums=[1,2,4,3,6,5]
n=len(nums)
ret=[-1 for i in range(n)]
stack=nums[::-1]
for i in range(n-1,-1,-1):
    while stack and stack[-1]<=nums[i]:
        stack.pop()
    if stack:
        ret[i]=stack[-1]
    stack.append(nums[i])
print(ret)