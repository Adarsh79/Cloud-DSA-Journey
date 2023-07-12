# Write a recursive function to convert a given string into the number it represents.
# That is input will be a numeric string that contains only numbers,
# you need to convert the string into corresponding integer and return the answer.
# Sample Input 1 :
# 00001231
# Sample Output 1 :
# 1231
# Sample Input 2 :
# 12567
# Sample Output 2 :
# 12567

def string_integer(string):
    if len(string) <= 1:
        return ord(string[0]) - ord("0")

    sub_str = string_integer(string[1:])

    newInt = (ord(string[0]) - ord("0")) * (10 ** (len(string) - 1)) + sub_str

    return newInt


print(string_integer("00120217810"))
