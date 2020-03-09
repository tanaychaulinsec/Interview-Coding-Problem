def fac(x):
    res=1
    for i in range(1,x+1) :
        res*=i
    print ("Factorial of {} is {}".format(x,res))

n=int(input("Enter a number"))
fac(5)

