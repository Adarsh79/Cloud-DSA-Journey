def is_palindrome(s):
    return check_palindrome(s)


def reverse(s):
    n = len(s)
    if n <= 1:
        return s
    left, right = s[0], s[n-1]
    substring = s[1:n-1]
    return right + reverse(substring) + left


def check_palindrome(s):
    n = len(s)
    if n <= 1:
        return True
    if s[0] == s[n-1]:
        substring = s[1:n-1]
        return check_palindrome(substring)
    return False


string = "mom"
print(is_palindrome(string))
