import math
'''def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)'''
''''def Fibonacci(n):
    a=0
    b=1
    if n<0:
        print("Invalid Input")
    elif n==0:
        return a
    elif n==1:
        return b
    else :
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return c'''

def fibonacciOptimized(n):
    #O(1)T O(1)s

    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))
def fast_fibonacci(n):
    a = [0, 1]
    for i in range(2, n+1):
        a.insert(i, a[i - 1] + a[i - 2])
    return a[n]
n=int(input())
print(fast_fibonacci(n))
print(fibonacciOptimized(n))