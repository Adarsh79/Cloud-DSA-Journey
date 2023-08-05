# Given a list of random characters, when we encounter list elements P and I,
# we need to replace ["P", "I"] with ["3", ".", "1", "4"]
# To do that you need to make a space by shifting the characters to the right.

def replace_pi(x):
    return replace_chars(x, 0)


def replace_chars(x, f):
    if len(x) < 2 or f == len(x):
        return x
    if x[f] == "P" and x[f+1] == "I":
        x[f:f+2] = ["3", ".", "1", "4"]
        return replace_chars(x, f+1)
    return replace_chars(x, f+1)


source = ["1", "2", "12093", "P", "I", "618", "P", "I", "9"]
print(replace_pi(source))
