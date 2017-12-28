def merge_the_tools(string, k):
    t = [string[i:i+k] for i in range(0,len(string),k)]
    u = []
    for i in enumerate(t):
        u.append(''.join([b for a,b in enumerate(t[i]) if b not in t[i][:a]]))
    for i in enumerate(u):
        print(u[i])
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)