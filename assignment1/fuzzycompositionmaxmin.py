def inputMatrix(which):
    row = int(input(f"Enter the number of rows for the {which} matrix:\n"))
    matrix = []
    for i in range(0, row):
        mat_row = [float(a) for a in input(
            f"Enter {i+1}th row as space separated list:\n").split(" ")]
        matrix.append(mat_row)
    return matrix


matrix1 = inputMatrix("first")
print("")
matrix2 = inputMatrix("second")


def getMaxMinComposition(matrix1, matrix2):
    row1 = len(matrix1)
    col2 = len(matrix2[0])
    row2 = len(matrix2)

    matrix3 = []
    for i in range(0, row1):
        li = []
        for j in range(0, col2):
            res = 0
            for k in range(0, row2):
                res = max(res, min(matrix1[i][k], matrix2[k][j]))
            li.append(res)
        matrix3.append(li)
    return matrix3


print("\nThe resultant matrix:\n", getMaxMinComposition(matrix1, matrix2))

# SAMPLE OUTPUT
###############

# Inputs
# ------
# Enter the number of rows for the first matrix:
# 2
# Enter 1th row as space separated list:
# 0.7 0.5 0.2
# Enter 2th row as space separated list:
# 0.1 0.4 0.6

# Enter the number of rows for the second matrix:
# 2
# Enter 1th row as space separated list:
# 0.2 0.9
# Enter 2th row as space separated list:
# 0.7 0.1

# Outputs
# -------
# The resultant matrix:
#  [[0.5, 0.7], [0.4, 0.1]]
