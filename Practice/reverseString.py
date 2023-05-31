def reverse(string):
    n = len(string)
    if n <= 1:
        return string
    left, right = string[0], string[n-1]
    substring = string[1:n-1]
    return right + reverse(substring) + left


x = "hello"
print(reverse(x))
