nums = [2, 7, 11, 15]
target = int(input())
ouput = 0
for i in range(len(nums)):
    output = target - nums[i]
    if (output in nums) and (nums.index(output) != i):
        break

    first_indx = i
    second_indx = nums.index(output)
    print([first_indx, second_indx])
