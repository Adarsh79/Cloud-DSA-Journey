# Given string we have to remove characters x from the string.

def updated_string(x):
    if len(x) == 0:
        return None
    return updated_list(0, x)


def updated_list(i, x):
    if i == len(x):
        return x
    # value = ""
    if x[i] == "x" and i < len(x):
        x[i] = x[i+1]
        # x[i] = " "
        # return updated_list(i, x)
    return updated_list(i+1, x)


name = "xxxxxxxx"
name = list(name)
print(updated_string(name))
