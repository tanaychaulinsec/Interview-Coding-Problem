class Solution:
    def productExceptSelf(nums) :

        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
nums=[1,2,4,5]
print(Solution.productExceptSelf(nums))