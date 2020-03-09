#python3
n=int(input())
lcoin=0
mcoin=0
scoin=0
while(n>0):
    if n>=10:
        lcoin+=n//10
        n=n%10
    elif n>=5:
        mcoin+=n//5
        n=n%5
    else:
        scoin+=n//1
        n=n%1
print(lcoin+mcoin+scoin)
