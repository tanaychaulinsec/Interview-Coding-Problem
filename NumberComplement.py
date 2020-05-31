def findComplement(num):
    res = ''
    for i in bin(num).replace("0b", ""):
        if i == '0':
            res += '1'
        else:
            res += '0'
    return int(res, 2)
num=23
print(findComplement(num))