a=[-2,-3,4-1,-2,5,1]
max_ending=0
max_ending_so_far=0
for i in range(len(a)):
    max_ending+=a[i]
    if max_ending>max_ending_so_far:
        max_ending_so_far=max_ending
    if max_ending<0:
        max_ending=0
print(max_ending_so_far)