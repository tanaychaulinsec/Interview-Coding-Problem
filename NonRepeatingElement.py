nums=[1,4,2,3,4,5,3,5,2,9,200,]
list=nums.copy()
for i in range(len(nums)):
    list.pop(0)
    if nums[i] in list:
        list.append(nums[i])
    else:
        print (nums[i])
