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
            if mat[i][j] == 1 and mat[j][i] != 1:
                print("The relation is not symmetric")
                return False
    return True


def checkTransitive(mat):
    r = len(mat)
    for p1 in range(0, r):
        for p2 in range(0, r):
            for p3 in range(0, r):
                if p1 != p2 and p2 != p3 and p1 != p3:
                    if mat[p1][p2] == 1 and mat[p2][p3] == 1 and mat[p1][p3] != 1:
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
# Enter number of rows: 5
# Enter the matrix
# 1 1 0 0 1
# 1 1 0 0 1
# 0 0 1 1 0
# 0 0 1 1 0
# 1 1 0 0 1

# Sample Output:
# ==============
# The relation is a equivalence relation.
