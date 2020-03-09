arr=[5,5,10,100,10,5]
OddSum,EvenSum=0,0
for i in range(len(arr)):
    if i%2==0:
        OddSum+=arr[i]
    else:
        EvenSum+=arr[i]
if OddSum>EvenSum:
    print(OddSum)
else:
    print(EvenSum)
