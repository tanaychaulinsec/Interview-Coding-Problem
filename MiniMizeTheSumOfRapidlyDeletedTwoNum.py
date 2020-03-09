
def getMinSum(arr):
    l=len(arr)
    sum=0
    while l>1:
            r_sum= arr[0] + arr[1]
            arr.pop(0)
            arr.pop(0)
            arr.insert(0,r_sum)
            sum+=r_sum
            l=len(arr)
    return sum
arr=[4,2,7,6,9]
print(getMinSum(arr))



