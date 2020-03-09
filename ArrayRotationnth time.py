arr=[1,2,3,4,5,6,7,8]
r=int(input())
n=len(arr)
arrNew=[0]*n
res=n-1-r%n
for i in range(n):
    arrNew[res-i]=arr[n-i-1]
print(arrNew)