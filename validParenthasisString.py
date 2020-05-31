def isValid( s):
    left = right = 0
    str_len=len(s)
    for i in range(str_len):
        left += 1 if s[i] in '(*' else -1
        if left < 0:
            return False
        right += 1 if s[str_len - 1 - i] in '*)' else -1
        if right < 0:
            return False

    return True
s="(*))"
print(isValid(s))