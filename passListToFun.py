def count(list):
    even=0
    odd=0
    for i in list :
        if i%2==0 :
            even+=1
        else :
            odd+=1
    return even,odd
list=[20,34,87,90,67,65,88,28,97]
even,odd= count(list)
print("Even :{} and odd :{}".format(even,odd))