### Median in a stream of integers (running integers)

### Examples

### After reading 1st element of stream - 5 -> median - 5
### After reading 2nd element of stream - 5, 15 -> median - 10
### After reading 3rd element of stream - 5, 15, 1 -> median - 5
### After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

# ''''''1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Media - 5.5
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# Media - 6'''''''''


def findmedian(newArr, n):
    sorted(newArr)
    if n % 2 is not 0:
        return float(newArr[n / 2])
    return float((newArr[int((n - 1) / 2)] + newArr[int(n / 2)]) / 2.0)


arr = [1, 3, 4, 5, 7, 6, 8, 9, 10]
newelement = [input()]
arr.append(newelement)
n = len(arr)
print("Our median =", findmedian(arr, n))