def print_formatted(number):
    s=len(bin(number)[2:])
    for i in range(1,number+1):
        print(repr(i).rjust(s),oct(i)[2:].rjust(s+1),hex(i)[2:].upper().rjust(s+1),bin(i)[2:].rjust(s+1))
    
    # your code goes here
if __name__ == '__main__':
    print_formatted(17)
 