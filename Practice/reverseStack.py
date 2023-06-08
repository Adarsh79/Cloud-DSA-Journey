def reverse(s):
    stack = []
    for i in s:
        stack.append(i)
    s = ""
    for i in range(len(stack)):
        s += stack.pop()
    return s


input_string = "Adarsh"
print(reverse(input_string))
