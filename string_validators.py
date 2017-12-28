if __name__ == '__main__':
    s = input()
    s_isalnum=[]
    s_isalpha=[]
    s_isdigit=[]
    s_islower=[]
    s_isupper=[]
    for i in range(len(s)):
        if s[i].isalnum() == True:
            s_isalnum.append(1)
        if s[i].isalpha() == True:
            s_isalpha.append(1)
        if s[i].isdigit() == True:
            s_isdigit.append(1)
        if s[i].islower() == True:
            s_islower.append(1)
        if s[i].isupper() == True:
            s_isupper.append(1)
    if len(s_isalnum)>0:
        print(True)
    else:
        print(False)
    if len(s_isalpha)>0:
        print(True)
    else:
        print(False)
    if len(s_isdigit)>0:
        print(True)
    else:
        print(False)     
    if len(s_islower)>0:
        print(True)
    else:
        print(False)     
    if len(s_isupper)>0:
        print(True)
    else:
        print(False)  

'''Editorial
S = raw_input()
print any([char.isalnum() for char in S])
print any([char.isalpha() for char in S])
print any([char.isdigit() for char in S])
print any([char.islower() for char in S])
print any([char.isupper() for char in S])
'''