def arrayManipulation(n, queries):
    arr = [0] * n
    max_el = 0
    for query in queries:
        l, r, val = query
        for i in range(l-1, r):
            arr[i] += val
            if arr[i] > max_el:
                max_el = arr[i]
    return max_el

a = [1,2,3,4,5]
a[1:3] += [7,8]
print(a)