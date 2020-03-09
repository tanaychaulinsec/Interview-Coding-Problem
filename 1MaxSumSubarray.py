#|-2|-3|4|-1|-2|1|5|-3|
arr=list(map(int,input().split(' ')))
max_end_here=max_so_far=0
for i in arr:
    max_end_here+=i
    if max_end_here<0:
        max_end_here=0
    if max_so_far<max_end_here:
        max_so_far=max_end_here
print(max_so_far)

