from array import *
from numpy import *
arr=array('i',[])
n=int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("enter the number"))
    arr.append(x)
start=0
print(arr)
val=int(input("enter number to be search in array"))
for e in arr :
    if e==val :
        break
    start+=1


print(start)