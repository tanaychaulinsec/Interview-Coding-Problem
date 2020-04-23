def isValid( s):
    dict = {')': '(', ']': '[', '}': '{'}
    stack = []

    for par in s:
        if par in dict.values():
            stack.append(par)
        elif stack and stack[-1] == dict[par]:
            stack.pop()
        else:
            return False

    return False if stack else True
s="())"
print(isValid(s))