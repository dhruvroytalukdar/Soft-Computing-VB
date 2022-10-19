def inputMatrix(which):
    row = int(input(f"Enter the number of rows for the {which} matrix:\n"))
    matrix = []
    for i in range(0, row):
        mat_row = [int(a) for a in input(
            f"Enter {i+1}th row as space separated list:\n").split(" ")]
        matrix.append(mat_row)
    return matrix


matrix1 = inputMatrix("first")
print("")
matrix2 = inputMatrix("second")


def getMaxDotComposition(matrix1, matrix2):
    row1 = len(matrix1)
    col2 = len(matrix2[0])
    row2 = len(matrix2)

    matrix3 = []
    for i in range(0, row1):
        li = []
        for j in range(0, col2):
            res = 0
            for k in range(0, row2):
                res = max(res, matrix1[i][k] * matrix2[k][j])
            li.append(res)
        matrix3.append(li)
    return matrix3


print("\nThe resultant matrix:\n", getMaxDotComposition(matrix1, matrix2))

# SAMPLE RUN
############

# Inputs
# ------
# Enter the number of rows for the first matrix:
# 3
# Enter 1th row as space separated list:
# 1 0 1 0
# Enter 2th row as space separated list:
# 0 0 0 1
# Enter 3th row as space separated list:
# 0 0 0 0

# Enter the number of rows for the second matrix:
# 4
# Enter 1th row as space separated list:
# 0 1
# Enter 2th row as space separated list:
# 0 0
# Enter 3th row as space separated list:
# 0 1
# Enter 4th row as space separated list:
# 0 0

# Outputs
# -------
# The resultant matrix:
#  [[0, 1], [0, 0], [0, 0]]
