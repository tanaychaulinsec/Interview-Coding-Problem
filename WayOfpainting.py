modd = 1000000007


# Function for finding the power
def power(x, y, p):
    res = 1  # Initialize result

    x = x % p  # Update x if it is more
    # than or equal to p

    while (y > 0):

        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p

            # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


# Function to calculate the number of ways
def ways(n, m):
    # Answer must be modulo of 10^9 + 7
    return power(m - 1, n - 1, modd) * m % modd


# Driver code
n, m = 5, 5
print(ways(n, m))