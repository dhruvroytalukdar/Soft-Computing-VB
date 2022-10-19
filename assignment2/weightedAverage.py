def y_value(x_val, x2, y2, x1, y1):
    slope = float(y2-y1)/(x2-x1)
    b = y2 - x2*slope
    return (x_val*slope + b)


n = int(input("Enter the number of fuzzy sets:\n"))

mul = 0.0
degrees = 0.0

for i in range(0, n):
    v = [float(i) for i in input(
        "Enter the values of set space separated:\n").split(" ")]
    d = [float(i)
         for i in input("Enter the degrees space separated:\n").split(" ")]
    assert(len(v) == len(d))
    avg = sum(v)/len(v)
    for i in range(0, len(v)-1):
        if v[i] <= avg <= v[i+1]:
            y_val = y_value(avg, v[i+1], d[i+1], v[i], d[i])
    mul += (avg * y_val)
    degrees += y_val

print("The defuzzified value is ", mul/degrees)

# OUTPUT
# Enter the number of fuzzy sets:
# 3
# Enter the values of set space separated:
# 0 1 2 3 4 5
# Enter the degrees space separated:
# 0 0.3 0.3 0.3 0.3 0
# Enter the values of set space separated:
# 3 4 5 6 7
# Enter the degrees space separated:
# 0 0.5 0.5 0.5 0
# Enter the values of set space separated:
# 5 6 7 8
# Enter the degrees space separated:
# 0 1 1 0
# The defuzzified value is  5.416666666666667
