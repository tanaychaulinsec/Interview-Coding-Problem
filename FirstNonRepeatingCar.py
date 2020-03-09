import sys
from time import time as t
MAX_CHAR = 256
def findFirstNonRepeating():
    # inDLL[x] contains pointer to a DLL node if x is present
    # in DLL. If x is not present, then inDLL[x] is NULL
    inDLL = [] * MAX_CHAR
    #repeated = [False] * MAX_CHAR
    # Let us consider following stream and see the process
    stream = "geegwks"
    j=-1
    for i in range(len(stream)//2+1):
        x = stream[i]
        y=stream[j-i]
        print("Reading " + x + " from stream")
        if x!=y:
            if x and y not in inDLL:
                inDLL.append(x)
                inDLL.append(y)
            else:
                inDLL.remove(x)
                inDLL.remove(y)
        else:
            if x not in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)

    return inDLL[0]
        # Driver program
print(findFirstNonRepeating())
