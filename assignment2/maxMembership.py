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

res = []
for i in range(0, len(values)):
    if degrees[i] == max(degrees):
        res.append(values[i])

print("The defuzzified value(s) are", res)

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
# The defuzzified value(s) are [6.0, 7.0]
