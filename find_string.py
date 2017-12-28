def count_substring(string, sub_string):
    s = len(string)
    ss = len(sub_string)
    count = 0
    for i in range(0, s-ss+1):
        if string[i:i+ss] == sub_string:
            count += 1
    return count