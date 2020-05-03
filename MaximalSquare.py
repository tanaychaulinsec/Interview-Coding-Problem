def maximalSquare(matrix):
    if not matrix: return 0
    dp = [[0 if matrix[row][col] == '0' else 1 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] == '1':
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
    res = max([max(row) for row in dp])
    return res ** 2
matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))