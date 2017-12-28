def capitalize(string):
    string_capitalize=string.capitalize()
    for i in range(len(string_capitalize)):
        if string_capitalize[i]==' ' and string_capitalize[i+1].isalpha():
            string_capitalize=string_capitalize[:i+1]+string_capitalize[i+1].upper()+string_capitalize[i+2:]
    return string_capitalize

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)