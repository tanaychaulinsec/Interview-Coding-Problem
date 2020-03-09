def minJumpsOptimal(arr, n):
   ladder=arr[0]
   stair=arr[0]
   jump=1
   for level in range(1,n+1):
       if level==n-1:
           return jump
       if level+arr[level]>ladder:
           ladder=level+arr[level]
       stair-=1
       if stair==0:
           jump+=1
           stair=ladder-level
   return jump
def minJumps(arr, n):
    jumps = [0 for i in range(n)]
    if (n == 0) or (arr[0] == 0):
        return float('inf')
    jumps[0] = 0
    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]
# Driver program to test above function
arr = [3,2,1,0,43,2,1,0,4]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, n))
print('Minimum number of jumps to reach',
      'end is', minJumpsOptimal(arr, n ))