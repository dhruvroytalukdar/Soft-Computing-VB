r = int(input("Enter number of rows: "))

mat = []
print("Enter the matrix")
for i in range(0, r):
    mat.append([float(i) for i in input().split(" ")])


def checkReflexive(mat):
    r = len(mat)
    for i in range(0, r):
        if mat[i][i] != 1:
            print("The relation is not reflexive")
            return False
    return True


def checkSymmetric(mat):
    r = len(mat)
    for i in range(0, r):
        for j in range(0, r):
            if mat[i][j] != mat[j][i]:
                print("The relation is not symmetric")
                return False
    return True


def checkTransitive(mat):
    r = len(mat)
    for p1 in range(0, r):
        for p2 in range(0, r):
            for p3 in range(0, r):
                if p1 != p2 and p2 != p3 and p1 != p3:
                    if mat[p1][p3] < min(mat[p1][p2], mat[p2][p3]):
                        print(
                            f"The relation is not transitive at {p1, p2} and {p2,p3}")
                        return False
    return True


def checkEquivalence(mat):
    return checkReflexive(mat) and checkSymmetric(mat) and checkTransitive(mat)


print("The relation is an equivalence relation." if checkEquivalence(
    mat) else "The relation is not an equivalence relation.")

# Sample Input:
# =============
# Enter number of rows: 3
# Enter the matrix
# 1 0.8 1
# 0.8 1 0.4
# 1 0.4 1

# Sample Output:
# ==============
# The relation is not transitive at (1, 0) and (0, 2)
# The relation is not an equivalence relation.
