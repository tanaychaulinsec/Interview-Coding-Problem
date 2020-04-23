from collections import deque
class Solution:
    def stringShift(self, s: str, shift): 
        res= deque(s)
        for direction, amount in shift:
            if direction == 0:
                res.rotate(-amount)
            else:
                res.rotate(amount)
        return "".join(res)


s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
print(Solution().stringShift(s,shift))