a = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
# a = [input() for _ in range(n)]
n = len(a)
c, desc_buf = [1] * n, []

for i in range(1, n):
    if a[i] < a[i - 1]:
        if not desc_buf:
            desc_buf = [i-1]
        desc_buf.append(i)
        if not i == n-1:
            continue
    if a[i] > a[i - 1]:
        c[i] = c[i - 1] + 1
    if desc_buf:
            for i_des, x in enumerate(desc_buf[::-1]):
                c[x] = max(c[x], i_des + 1)
            del desc_buf[:]
print(c)
print(a[:])
