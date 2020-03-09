def editDistance(str1,str2,m,n):
    '''if m<1:
        return n
    if n<1:
        return m
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    return 1 + min(editDistance(str1,str2,m,n-1),
    editDistance(str1, str2, m-1, n),
    editDistance(str1, str2, m-1, n - 1))''' ###Time Complexity is O(3^m) so need optimal solution
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j  # Min. operations = j

            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

str1 = "cat"
str2 = "cut"
print(editDistance(str1,str2,len(str1),len(str2)))