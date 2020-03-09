def multiply(x,y):
    if y==0:
        return  0
    if y>0:
        return x + multiply(x,y-1)
    if y<0:
        return -multiply(x,-y)

x=10
y=-5
print(multiply(x,y))