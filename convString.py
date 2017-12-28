# 递归，转化数字为任意基数的字符串
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(1453, 16))