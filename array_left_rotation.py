def array_left_rotation(a, n, k):
    a1 =  a[:k]
    a2 = a[k:]
    print(a1)
    print(a2)
    c = a2.extend(a1)
    print(c)
    print(type(c))
    return a2.extend(a1)

n, k = 5, 4
a = [1,2,3,4,5]
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
