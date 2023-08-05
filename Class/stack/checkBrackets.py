def check_brackets(x):
    stack = []

    for i in x:
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            bracket = stack.pop()
            if bracket == "(":
                if i != ")":
                    return False
            if bracket == "[":
                if i != "]":
                    return False
            if bracket == "{":
                if i != "}":
                    return False

    if stack:
        return False
    else:
        return True


inp = "{}[]"
print(check_brackets(inp))

