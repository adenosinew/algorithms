def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

testlist = [1,2,3,4,8,32,35,14,6,0]
print(sequentialSearch(testlist, 3))

