n = int(input("Enter the number of fuzzy sets:\n"))
values = []
degrees = []
for i in range(0, n):
    v = [float(i) for i in input(
        "Enter the values of set space separated:\n").split(" ")]
    d = [float(i)
         for i in input("Enter the degrees space separated:\n").split(" ")]
    assert(len(v) == len(d))
    values.append(v)
    degrees.append(d)

INTERVAL = 0.08


def y_value(x_val, x2, y2, x1, y1):
    slope = float(y2-y1)/(x2-x1)
    b = y2 - x2*slope
    return (x_val*slope + b)


def find_area(value1, degree1, value2, degree2):
    area = 0.0
    x1 = value1
    while x1 < value2:
        x2 = x1 + INTERVAL
        curr_area = (
            INTERVAL*(y_value(x1, value2, degree2, value1, degree1) + y_value(x2, value2, degree2, value1, degree1))/2)
        area += curr_area
        x1 += INTERVAL
    return area


index = 0
store = -1
for i in range(0, n):
    v_list = values[i]
    d_list = degrees[i]
    area = 0.0
    for j in range(0, len(v_list)-1):
        area += find_area(v_list[j], d_list[j], v_list[j+1], d_list[j+1])
    if store < area:
        store = area
        index = i

val = sum((values[index])) / len(values[index])
print("The defuzzified value is ", val)

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
# The defuzzified value is  6.5
