def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionofMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionofMax]:
                positionofMax = location

        alist[fillslot], alist[positionofMax] = alist[positionofMax], alist[fillslot]


alist = [54,25,94,17,77,31,44,55,20]
selectionSort(alist)
print(alist)