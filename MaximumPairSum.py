n=int(input())
arr=list(map(int,input().split()[:n]))
print(*(arr))
largest=arr[0]
smallest=arr[0]
Second_Largest=None
Second_smallest=None
for num in arr[1:]:
    if num>largest:
        Second_Largest=largest
        largest=num
    elif Second_Largest==None or num>Second_Largest:
        Second_Largest=num
    if num<smallest:
        Second_smallest=smallest
        smallest=num
    elif Second_Largest==None or num<Second_Largest:
        Second_Largest=num
print(largest,Second_Largest,smallest,Second_smallest)



