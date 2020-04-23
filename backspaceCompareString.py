def backspaceCompare(S, T):
    def backspc(s, i):
        bks = 0
        while i >= 0 and (s[i] == '#' or bks > 0):
            if s[i] == '#':
                bks += 1
            else:
                bks -= 1
            i -= 1
        return i

    i, j = len(S) - 1, len(T) - 1
    while True:
        i = backspc(S, i)
        j = backspc(T, j)
        if i < 0 and j < 0:
            return True
        if i >= 0 and j >= 0 and S[i] == T[j]:
            i -= 1
            j -= 1
        else:
            break
    return False
S = "ab#c"
T = "ad#c"
print(backspaceCompare(S,T))