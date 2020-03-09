def find_gcd(x,y):
    while y:
        x,y=y,x % y
    return x
a=[4,16,8,24,32]
num1=a[0]
num2=a[1]
gcd=find_gcd(num1,num2)
for i in range(2,len(a)):
    gcd=find_gcd(a[i],gcd)
print(gcd)