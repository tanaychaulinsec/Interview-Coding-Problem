a = [4,6,4,5,6,2]
#a = [input() for _ in range(n)]
n=len(a)
c, desc_buf = [1]*n, []

for i in range(1, n):
    if a[i] < a[i-1]:
        #if this condition satisfy then we store the value in buffer
        #if not desc_buf:
        desc_buf = [i-1]
        desc_buf.append(i)
        if i != n-1:
            continue
    if a[i] > a[i-1]:
        c[i] = c[i-1] + 1
    if desc_buf :
        #check buffer last to start like decs_buf[::-1] [::-2]..... as per element exist in buffer
        for extra, idx in enumerate(desc_buf[::-1]):
           c[idx] = max(c[idx], extra + 1)
        del desc_buf[:]

print (*(c))