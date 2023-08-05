# Given string we have to remove characters x from the string.

def new_string(s, key):
    if len(s) == 0:
        return ""
    if s[0] == key:
        return new_string(s[1:], key)
    return s[0] + new_string(s[1:], key)


string = input("Enter a string: ")
print(new_string(string, "x"))
