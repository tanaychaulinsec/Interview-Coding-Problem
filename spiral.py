def spiralMatrix(matrix):
    if not matrix:
        return []
    top, left = 0, 0
    right, buttom = len(matrix[0]) - 1, len(matrix) - 1
    newMatrix = []
    while top <= buttom and left <= right:
        # Step 1 :- From Top left to Top right
        for i in range(left, right + 1):
            newMatrix.append(matrix[top][i])
        top += 1
        # Step 2 :-From right Top to right Buttom
        for i in range(top, buttom + 1):
            newMatrix.append(matrix[i][right])
        right -= 1

        # Step 3 :- from Buttom right To Buttom left
        if top <= buttom:
            for i in range(right, left - 1, -1):
                newMatrix.append(matrix[buttom][i])
            buttom -= 1

        # Step 4 :- from left Buttom to left Top
        if left <= right:
            for i in range(buttom, top - 1, -1):
                newMatrix.append(matrix[i][left])
            left += 1
    return newMatrix

matrix=[[3],[4],[5]]
print(spiralMatrix(matrix))