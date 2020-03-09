def tripletsSum(arr,n):
    found=False
    arr.sort()
    for i in range(0,n-2):
            l=i+1
            r=n-1
            while l<r:
                sum=arr[i]+arr[r]+arr[l]
                if sum==0:
                    l+=1
                    r-=1
                    found=True
                    print(arr[i],arr[r],arr[l])
                elif sum<0:
                    l+=1
                else:
                    r-=1
    if (found==False):
        print("Triplets Not Found!")
arr=[0,-1,2,-3,1]
tripletsSum(arr,len(arr))