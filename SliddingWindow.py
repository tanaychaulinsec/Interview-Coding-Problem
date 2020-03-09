def printMax(arr, n, k):


    for i in range(n - k):
        sum=max(arr[i],arr[i+1],arr[i+2])
        print((sum))

    # Driver method


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3
    printMax(arr, n, k) 