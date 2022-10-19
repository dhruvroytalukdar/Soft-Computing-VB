n = int(input("Enter the number of fuzzy sets:\n"))
mp = {}
for i in range(0, n):
    v = [float(i) for i in input(
        "Enter the values of set space separated:\n").split(" ")]
    d = [float(i)
         for i in input("Enter the degrees space separated:\n").split(" ")]
    assert(len(v) == len(d))
    for i in range(0, len(v)):
        if v[i] in mp.keys():
            mp[v[i]] = max(mp[v[i]], d[i])
        else:
            mp[v[i]] = d[i]

values = list(mp.keys())
degrees = list(mp.values())

INTERVAL = 0.08


def y_value(x_val, x2, y2, x1, y1):
    slope = float(y2-y1)/(x2-x1)
    b = y2 - x2*slope
    return (x_val*slope + b)


areaXxbar = 0.0
area = 0.0
for i in range(0, len(values)-1):
    x1 = values[i]
    while x1 < values[i+1]:
        x2 = x1 + INTERVAL
        curr_area = (
            INTERVAL*(y_value(x1, values[i+1], degrees[i+1], values[i], degrees[i]) + y_value(x2, values[i+1], degrees[i+1], values[i], degrees[i]))/2)
        area += curr_area
        areaXxbar += (curr_area * ((x1+x2)/2))
        x1 += INTERVAL

print("The defuzzified value is ", areaXxbar/area)

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
# The defuzzified value is  4.948717948717948