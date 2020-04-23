def andOperator(a, b):
    while (a < b):
        # -b is the 2's complement of b
        # when do bitwise or with b we
        # get LSB and we subtract that from b
        c=bin(-b).replace("0b", "")
        b-= (b & -b)
    return b


# Driver code
a, b = 5, 7
print(andOperator(a, b))