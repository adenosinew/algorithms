def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]


alist = [54,25,94,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)