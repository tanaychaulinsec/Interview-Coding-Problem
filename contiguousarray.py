class Solution:
    def findMaxLength(nums):
        nums=[x if x else -1 for x in nums]
        prefixSum={0:-1}
        presum=res=0
        for i,x in enumerate(nums):
            presum+=x
            if presum in prefixSum:
                res=max(res,i-prefixSum[presum])
            else:
                prefixSum[presum]=i
        return res

    nums=[0,1,1,0]
    print(findMaxLength(nums))