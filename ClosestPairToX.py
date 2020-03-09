arr=[5,6,7,8,9,12,14]
x=21
l=0
r=len(arr)-1
diff=x
while l<r:
    if abs(arr[l]+arr[r]-x)<diff:
        diff=abs(arr[l]+arr[r]-x)
        res_l=arr[l]
        res_r=arr[r]
    elif arr[l]+arr[r]>x:
        r-=1
    else:
        l+=1
print(res_l,res_r)

