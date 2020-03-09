import sys

INT_MIN = -sys.maxsize - 1


def maxSum(arr, n, k):
    # n must be greater than k
    if not n > k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    max_sum = INT_MIN
    max_sum_1 = sum([arr[i] for i in range(k)])

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(n - k):
        window_sum = max_sum_1 - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum,max_sum_1)
        max_sum_1=window_sum

    return max_sum


# Driver code
arr = [7, 4, 22, 10, 21, 3, 1, 9, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))