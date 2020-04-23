from collections import defaultdict
def subarrayEqualsK (nums,k):
    dic=defaultdict(int)
    subarray_count=preSum=0
    for num in nums:
        preSum+=num
        if preSum-k in dic:
            subarray_count+=dic[preSum-k]
        if preSum==k:
            subarray_count+=1

        dic[preSum]+=1
    return subarray_count
    # res = 0
    # for i in range(len(nums)):
    #     sum=0
    #     for j in range(i,len(nums)):
    #         sum=sum+nums[j]
    #         if (sum == k):
    #             res+=1
    # return res
nums=[1,2,3,6,2,4]
k=6
print(subarrayEqualsK(nums,k))

