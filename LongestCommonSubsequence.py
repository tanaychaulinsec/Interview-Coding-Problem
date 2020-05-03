def longestCommonSubsequence(text1,text2):
    if len(text1) > len(text2):
        str1,str2 = text1,text2
    else:
        str1,str2= text2,text1
    dp = [[0 for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for row in range(len(str2)):
        for col in range(len(str1)):
            if str2[row ] == str1[col]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[row][col]



text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1,text2))