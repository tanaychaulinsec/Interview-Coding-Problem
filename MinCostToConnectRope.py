arr=[2,2,3,3,5,6,7,8,9,34,76,89,98,89,98,4566788990,3998765445678,34567898764,34567898654,689009865,345689098764,34568998764,34568998765,3456789009876,6543245678,34679876,34569876]
cur_sum=0
res_sum=0
arr.sort()
while(len(arr)>1):
    cur_sum=arr[0]+arr[1]
    arr.pop(0)
    arr.pop(0)
    arr.insert(0,cur_sum)
    res_sum+=cur_sum
print(res_sum)