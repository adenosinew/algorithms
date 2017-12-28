def print_rangoli(size):
    alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(size):
        if i>0:
            sub=alphabet[size-1-i:size]
            sub_reverse=sub[:]
            sub.reverse()
            sub_list=sub+sub_reverse[1:]
            s='-'.join(sub_list)
        else:
            s=alphabet[size-1]
        print(s.center(4*size-3,'-'))
    for i in range(size-2,-1,-1):
        if i>0:
            sub=alphabet[size-1-i:size]
            sub_reverse=sub[:]
            sub.reverse()
            sub_list=sub+sub_reverse[1:]
            s='-'.join(sub_list)
        else:
            s=alphabet[size-1]
        print(s.center(4*size-3,'-'))        



if __name__ == '__main__':
    print_rangoli(5)
